# 사용 패키지
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_samples, silhouette_score
import folium
from folium import plugins

# 사용 변수
sago = pd.read_csv('../데이터/전처리_21년대구사고지역시간좌표.csv')
sago = sago[sago['구']=='달서구']

sago_gps = sago[['lat','long']]
death_gps = pd.read_csv('../데이터/달서구_사망자.txt')

acc_df = pd.concat([sago_gps, death_gps])
acc_df2 = acc_df.copy()

mySeed = 7942

# 최적의 K 구하기 (엘보우)
Sum_of_squared_distances = []
K = range(1,10)
for num_clusters in K :
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(acc_df[['lat','long']])
    Sum_of_squared_distances.append(kmeans.inertia_)
plt.plot(K,Sum_of_squared_distances,'o-')
plt.xlabel('Number of clusters (K)') 
plt.ylabel('SSE') 
plt.title('Optimal k (Elbow method)')
plt.show()

# 최적의 K 구하리 (실루엣)
range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]
silhouette_avg = []
for num_clusters in range_n_clusters:
 
    # initialise kmeans
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(acc_df[['lat','long']])
    cluster_labels = kmeans.labels_
 
 # silhouette score
    silhouette_avg.append(silhouette_score(acc_df[['lat','long']], cluster_labels))
plt.plot(range_n_clusters,silhouette_avg,'o-')
plt.xlabel('Number of clusters (K)') 
plt.ylabel('Silhouette score') 
plt.title('Optimal k (Silhouette)')
plt.show()

# 최적의 K 구하기 (갭)
def optimalK(data, nrefs=3, maxClusters=15):
    gaps = np.zeros((len(range(1, maxClusters)),))
    resultsdf = pd.DataFrame({'clusterCount':[], 'gap':[]})
    for gap_index, k in enumerate(range(1, maxClusters)):
        refDisps = np.zeros(nrefs)
        for i in range(nrefs):
            randomReference = np.random.random_sample(size=data.shape)
            # fit
            km = KMeans(k)
            km.fit(randomReference)
            
            refDisp = km.inertia_
            refDisps[i] = refDisp
        km = KMeans(k)
        km.fit(data)
        
        origDisp = km.inertia_

        gap = np.log(np.mean(refDisps)) - np.log(origDisp)
        gaps[gap_index] = gap
        
        resultsdf = resultsdf.append({'clusterCount':k, 'gap':gap}, ignore_index=True)
    return (gaps.argmax() + 1, resultsdf)
score_g, df = optimalK(acc_df[['lat','long']], nrefs=5, maxClusters=10)
plt.plot(df['clusterCount'], df['gap'], linestyle='-', marker='o', color='b');
plt.xlabel('Number of clusters (K)');
plt.ylabel('Gap statistic');
plt.title('Optimal k (Gap statistic)');

# K-means
obj = KMeans(n_clusters=3, max_iter=300, algorithm='auto', random_state=mySeed)
model = obj.fit(acc_df)
pred = model.predict(acc_df)
centers = model.cluster_centers_
cent = pd.DataFrame(centers, columns=['lat', 'long'])

# center와 cluster dataframe을 저장
clusters = acc_df
clusters['cluster'] = pred

# cent.to_csv('../데이터/acc_centers.csv')
# clusters.to_csv('../데이터/acc_cluster.csv')

