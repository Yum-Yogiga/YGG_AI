import csv

input = open('test2.csv','r',encoding='utf-8')
output = open('test3.csv','w',encoding='utf-8',newline='')

csvReader = csv.reader(input)
csvWriter = csv.writer(output)

inputList = []

for line in csvReader:
    inputList.append(line)

keywordList=['음식이 맛있어요',
              '친절해요',
              '특별한 메뉴가 있어요',
              '매장이 청결해요',
              '재료가 신선해요',
              '가성비가 좋아요',
              '양이 많아요',
              '인테리어가 멋져요',
              '혼밥하기 좋아요']


outputList = [['가게이름',
              '음식이 맛있어요',
              '친절해요',
              '특별한 메뉴가 있어요',
              '매장이 청결해요',
              '재료가 신선해요',
              '가성비가 좋아요',
              '양이 많아요',
              '인테리어가 멋져요',
              '혼밥하기 좋아요',
              '링크']]

indexList = [1,3,5,7,9,11,13,15,17,19]

for ilist in inputList[1:]:
    templist = [ilist[0],0,0,0,0,0,0,0,0,0,ilist[-1]]   # 가게이름, 키워드 9개, 링크
    for idx in indexList:
        if ilist[idx] in keywordList:
            index = keywordList.index(ilist[idx])       # keyword 종류 찾기
            templist[index+1] = ilist[idx+1]            # 키워드 숫자 저장
    outputList.append(templist)

csvWriter.writerows(outputList)