# 사용 패키지
import pandas as pd
import folium
from folium import plugins

# 사용 변수
cent = pd.read_csv('../데이터/acc_centers.csv')
clusters = pd.read_csv('../데이터/acc_cluster.csv')
acc_df = pd.read_csv('../데이터/accidents_df.csv')

# folium 지도시각화로 3개 군집 시각화
map_dg = folium.Map(location=[35.8714354,128.601445], zoom_start=12)
folium.TileLayer('cartodbpositron').add_to(map_dg)
colors=['blue', 'green', 'gray']

for i in range(len(clusters.cluster.unique())): # k-means 로 설정한 수만큼 돌림
    sub_df = clusters[clusters['cluster']==i]
    for lat,long, num in zip(sub_df.lat, sub_df.long, sub_df.cluster):
        folium.features.CircleMarker(
            [lat, long],
            radius=3,
            color=colors[i%10],
            popup=[num, lat, long],
            fill=True,
            fill_color=colors[i%10],
            fill_opacity=0.6
        ).add_to(map_dg)

for lat,long in zip(cent.lat, cent.long): # cluster center
    folium.features.CircleMarker(
        [lat, long],
        radius=3,
        color='red',
        fill=True,
        popup=[lat,long],
        fill_color='red',
        fill_opacity=0.6
    ).add_to(map_dg)

map_dg


# folium 지도 시각화로 섬세 군집 분류
map_dg2 = folium.Map(location=[35.8714354,128.601445], zoom_start=12)

accidents = plugins.MarkerCluster().add_to(map_dg2)

for lat,long in zip(acc_df.lat, acc_df.long):
    folium.Marker(
        location=[lat, long],
        icon=None
    ).add_to(accidents)

map_dg2

