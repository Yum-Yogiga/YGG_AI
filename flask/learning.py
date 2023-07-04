import random

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
from sklearn.cluster import KMeans


# 표 출력
def print_df(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))


# 검색할 값 추가하기.
def add_want_keyword(data, keywords):
    data = data.append(pd.Series(keywords, index=data.columns), ignore_index=True)

    # index를 보기 편하게 미리 지정한 idx로 바꿈. 추후에 idx가 식당 이름이 될 것으로 예상
    data = data.set_index(keys=['가게이름'],drop=True)
    return data


# print(data)
# def get_restaurant(keywords):
#     # 저장된 파일 가져오기
#     data = pd.read_csv('sample.csv')
#     data = add_want_keyword(data,keywords)
#     # cosine similarity 계산
#     similarity_rate = cosine_similarity(data, data)
#     # print(similarity_rate)
#
#     # 계산한 값으로 유사도 표를 만듦
#     similarity_rate_df = pd.DataFrame(
#         data=similarity_rate,
#         index=data.index,
#         columns=data.index
#     )
#
#     # similarity_rate_df.head()
#
#     # 유사도 상위 5개 추천
#     indexes = similarity_rate_df['나의식당'].sort_values(ascending=False)[:6]
#
#     return indexes

def get_restaurant(keywords):
    # 저장된 파일 가져오기
    data = pd.read_csv('../crawling/percentage.csv')
    data = data.drop('링크',axis=1)
    data = add_want_keyword(data,keywords)
    # cosine similarity 계산
    similarity_rate = cosine_similarity(data, data)
    # print(similarity_rate)

    # 계산한 값으로 유사도 표를 만듦
    similarity_rate_df = pd.DataFrame(
        data=similarity_rate,
        index=data.index,
        columns=data.index
    )

    # similarity_rate_df.head()

    # 유사도 상위 5개 추천
    indexes = similarity_rate_df['나의식당'].sort_values(ascending=False)[1:6]

    return indexes.index.tolist()

# KMeans algorithms
def kmeans(keywords):
    # 저장된 파일 가져오기
    data = pd.read_csv('../crawling/percentage.csv')
    data = data.drop('링크', axis=1)
    data = data.drop('가게이름',axis=1)

    # 검색 후 가게이름을 위한 데이터 재로드
    after_data = pd.read_csv('../crawling/percentage.csv')

    #kmeans
    k = 9
    km_model = KMeans(n_clusters=k)
    km_model.fit(data)
    labels = km_model.labels_

    result = after_data[labels == km_model.predict([keywords])]['가게이름'].tolist()

    result = random.sample(result,5)

    return result
