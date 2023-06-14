import requests
import json
import config

# key 값 입력
REST_API_KEY = config.config['kakao']

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response


def chat_to_keyword(chat):
    # KoGPT에게 전달할 명령어 구성
    prompt = '''문장의 중요 키워드를 분류합니다.
                사용되는 키워드는 [맛, 가성비, 뷰, 서비스] 입니다.
                맛있고 가성비 좋고 풍경이 좋고 사람들이 친절한 곳 = [5,5,5,5]
                적당히 싸고 맛있게 먹고 싶어요 = [5,5,0,0]
                이쁘고 사람들이 친절한데 값도 나쁘지 않아요 = [0,5,5,5]
                싸고 맛있는 집 = [5,5,0,0]
                맛은 없어도 좋으니 최대한 싼곳 = [0,5,0,0]
                싸고 맛있고 이쁜 곳 = [5,5,5,0]
                
                '''

    # 파라미터를 전달해 kogpt_api()메서드 호출
    response = kogpt_api(
        prompt=prompt + chat + ' =',
        max_tokens=10,
        temperature=0.1,
        top_p=1.0,
        n=1
    )

    temp = response['generations'][0]['text'].strip()
    if temp[0] !='[' :
        temp = '[' + temp
    if temp[-1] != ']' :
        temp = temp + ']'

    result = eval(temp)

    for i in range(5):
        result.append(0)
    print(result)

    return result