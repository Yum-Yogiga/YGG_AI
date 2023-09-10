import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


import seaborn as sns
from learning import print_df
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap


f = pd.read_csv('./data/total.csv')
# 음식이 맛있어요	친절해요	특별한 메뉴가 있어요	매장이 청결해요	재료가 신선해요	가성비가 좋아요	양이 많아요	인테리어가 멋져요	혼밥하기 좋아요
data = f[['음식이 맛있어요','친절해요', '특별한 메뉴가 있어요']]

data['음식이 맛있어요'] = f['음식이 맛있어요'] / (f['음식이 맛있어요'] + f['친절해요'] + f['특별한 메뉴가 있어요'])
data['친절해요'] = f['친절해요'] / (f['음식이 맛있어요'] + f['친절해요'] + f['특별한 메뉴가 있어요'])
data['특별한 메뉴가 있어요'] = f['특별한 메뉴가 있어요'] / (f['음식이 맛있어요'] + f['친절해요'] + f['특별한 메뉴가 있어요'])

k = 3
km_model = KMeans(n_clusters=k)
km_model.fit(data)
labels = km_model.labels_

resultBySklearn = data.copy()
resultBySklearn["cluster"] = km_model.labels_

data = pd.DataFrame({'taste':resultBySklearn['음식이 맛있어요'],
                     'kindness':resultBySklearn['친절해요'],
                     'special':resultBySklearn['특별한 메뉴가 있어요'],
                     'cluster':resultBySklearn['cluster']})

centers = km_model.cluster_centers_

fig = plt.figure()
axes = fig.add_subplot(111,projection='3d')

for c in data.cluster.unique():
    axes.scatter(data.taste[data.cluster==c],data.kindness[data.cluster==c],data.special[data.cluster==c],label=c)
axes.set_xlabel('음식이 맛있어요')
axes.set_ylabel('친절해요')
axes.set_zlabel('특별한 메뉴가 있어요')
axes.legend()
plt.show()
fig.get_figure().savefig('valid.png')