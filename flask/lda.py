import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler

f = pd.read_csv('./data/total.csv')

data = f[['음식이 맛있어요','친절해요', '특별한 메뉴가 있어요','매장이 청결해요','재료가 신선해요',
          '가성비가 좋아요',	'양이 많아요',	'인테리어가 멋져요',	'혼밥하기 좋아요']]

k = 9
km_model = KMeans(n_clusters=k)
km_model.fit(data)
labels = km_model.labels_

resultBySklearn = data.copy()
pre_data = data.copy()
resultBySklearn["cluster"] = km_model.labels_

data = pd.DataFrame({'taste':resultBySklearn['음식이 맛있어요'],
                     'kindness':resultBySklearn['친절해요'],
                     'special':resultBySklearn['특별한 메뉴가 있어요'],
                     'clean':resultBySklearn['매장이 청결해요'],
                     'fresh':resultBySklearn['재료가 신선해요'],
                     'cost':resultBySklearn['가성비가 좋아요'],
                     'amount':resultBySklearn['양이 많아요'],
                     'interior':resultBySklearn['인테리어가 멋져요'],
                     'single':resultBySklearn['혼밥하기 좋아요'],
                     'target':resultBySklearn['cluster']})

data_scaled = StandardScaler().fit_transform(pre_data)

lda = LinearDiscriminantAnalysis(n_components=2)

lda.fit(data_scaled, data.target)
data_lda = lda.transform(data_scaled)

my_res = [0.3,0.3,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
restaurant = lda.transform([my_res])
print(data_lda.shape)

pred = lda.predict([my_res])
print(pred[0])
print(km_model.cluster_centers_[pred[0]])

lda_columns=['lda_component_1','lda_component_2']
irisDF_lda = pd.DataFrame(data_lda,columns=lda_columns)
irisDF_lda['target']=data.target

markers=['1','2','3','4','8','.','o','v','^','<','>']

for i in range(k):
    x_axis_data = irisDF_lda[irisDF_lda['target']==i]['lda_component_1']
    y_axis_data = irisDF_lda[irisDF_lda['target']==i]['lda_component_2']

    plt.scatter(x_axis_data, y_axis_data, marker='.',label=i)

plt.scatter(restaurant[0][0],restaurant[0][1],marker='x',label='res')

plt.legend(loc='upper right')
plt.xlabel('lda_component_1')
plt.ylabel('lda_component_2')
plt.plot()
plt.tight_layout()
plt.savefig('lda.png')