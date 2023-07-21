import random

import numpy as np
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
    # data = pd.concat([data, pd.Series(keywords, index=data.columns)])

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
    data,f = file_system()
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

def file_system():
    f = pd.read_csv('./data/total.csv')
    # 음식이 맛있어요	친절해요	특별한 메뉴가 있어요	매장이 청결해요	재료가 신선해요	가성비가 좋아요	양이 많아요	인테리어가 멋져요	혼밥하기 좋아요
    data = f[['가게이름','음식이 맛있어요','친절해요', '특별한 메뉴가 있어요','매장이 청결해요','재료가 신선해요', '가성비가 좋아요',	'양이 많아요',	'인테리어가 멋져요',	'혼밥하기 좋아요']]
    return data,f

# KMeans algorithms
def kmeans(keywords):
    # 저장된 파일 가져오기
    data, after_data = file_system()
    data.drop('가게이름',axis=1)
    #kmeans
    k = 9
    km_model = KMeans(n_clusters=k)
    km_model.fit(data)
    labels = km_model.labels_

    print(np.bincount(labels))
    print(km_model.predict([keywords]))
    print(km_model.cluster_centers_[km_model.predict([keywords])])

    result = after_data[labels == km_model.predict([keywords])]['가게이름'].tolist()

    result = random.sample(result,5)

    return result
