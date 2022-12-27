# 사망자 사고는 좌표까지 포함돼 있지만 부상자 사고는 좌표가 없다
# 직접 부상자 사고 좌표를 긁어와 사망자 데이터와 부상자 데이터를 합친다.

# 사용 패키지
import numpy as np
import pandas as pd

# 교통사고문선시스템에서 가져온 21녀도 보행자 사망 및 부상자 데이터
death21 = pd.read_csv('../데이터/21_deaths_dg.csv')
injury21 = pd.read_csv('../데이터/21_accidents_dg.csv')

# 직접 보행자 부상자 사고의 좌표를 긁어온 데이터
namgu = pd.read_csv(f'../데이터/대구보행자사고gps/남구.txt')
dalsuh = pd.read_csv(f'../데이터/대구보행자사고gps/달서구.txt')
dalsung = pd.read_csv(f'../데이터/대구보행자사고gps/달성군.txt')
donggu = pd.read_csv(f'../데이터/대구보행자사고gps/동구.txt')
bukgu = pd.read_csv(f'../데이터/대구보행자사고gps/북구.txt')
seogu = pd.read_csv(f'../데이터/대구보행자사고gps/서구.txt')
susunggu = pd.read_csv(f'../데이터/대구보행자사고gps/수성구.txt')
junggu = pd.read_csv(f'../데이터/대구보행자사고gps/중구.txt')
death = pd.read_csv(f'../데이터/대구보행자사고gps/사망자.txt')


# 불필요한 칼럼 지우고 시군구에서 구만 뽑아오기
injury21 = injury21[['사고번호', '사고일시', '시군구']]
injury21['구'] = [injury21['시군구'].str.split()[x][1] for x in range(0,len(injury21))]

death21 = death21[['사고번호', '사고일시', '시군구']]
death21['구'] = [death21['시군구'].str.split()[x][1] for x in range(0,len(death21))]


# 순서대로 따온 사고 좌표를 순서대로 알맞는 구에 입력한다
namgu21 = injury21[injury21['구']=='남구']
namgu21['lat'] = namgu.lat.values
namgu21['long'] = namgu.long.values

dalsuh21 = injury21[injury21['구']=='달서구']
dalsuh21['lat'] = dalsuh.lat.values
dalsuh21['long'] = dalsuh.long.values

dalsung21 = injury21[injury21['구']=='달성군']
dalsung21['lat'] = dalsung.lat.values
dalsung21['long'] = dalsung.long.values

donggu21 = injury21[injury21['구']=='동구']
donggu21['lat'] = donggu.lat.values
donggu21['long'] = donggu.long.values

bukgu21 = injury21[injury21['구']=='북구']
bukgu21['lat'] = bukgu.lat.values
bukgu21['long'] = bukgu.long.values

seogu21 = injury21[injury21['구']=='서구']
seogu21['lat'] = seogu.lat.values
seogu21['long'] = seogu.long.values

susunggu21 = injury21[injury21['구']=='수성구']
susunggu21['lat'] = susunggu.lat.values
susunggu21['long'] = susunggu.long.values

junggu21 = injury21[injury21['구']=='중구']
junggu21['lat'] = junggu.lat.values
junggu21['long'] = junggu.long.values

death21 = death21[['사고번호', '사고일시', '시군구']]
death21['lat'] = death.lat.values
death21['long'] = death.long.values


# 사고번호, 사고일시, 시군구, 수, lat, long의 dataframe을 만들고 저장
new_df = pd.DataFrame(columns=['사고번호', '사고일시', '시군구', '구', 'lat', 'long'])
dfs = [namgu21,
dalsuh21,
dalsung21,
donggu21,
bukgu21,
seogu21,
susunggu21,
junggu21,
death21]

for df in dfs:
    new_df = pd.concat([new_df, df])
    
new_df = new_df.sort_values('사고번호')
# new_df.to_csv('../데이터/전처리_21년대구전체사고및좌표.csv')

# 사고 시간대를 따로 추출하여 칼럼으로 두기
time_df = new_df
tmp=[]
for x in time_df['사고일시'].values:
    tmp.append(x[-3:-1])

time_df['시간'] = [int(t) for t in tmp]
# time_df.to_csv('../데이터/전처리_21년대구사고지역시간좌표.csv')


