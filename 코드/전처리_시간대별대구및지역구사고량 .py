# 사용 패키지
import pandas as pd

# 사용 변수
# 교통사고분석시스템에서 받아온 21년 대구 보행자 사고 (사망 + 부상자) 총 2116건
df = pd.read_csv('../데이터/21년대구보행자전체사고.csv')

# 사고번호, 사고일시, 시군구만 사용한다
new_df = df[['사고번호', '사고일시', '시군구']]

# 시군구만 따로 저장
sigun_df = new_df.sort_values('시군구')
sigun=sigun_df['시군구']

# 구단위로 저장
tmp_list = []
for s in sigun:
    tmp_list.append(s.split()[1])
sigun_df['구'] = tmp_list

# df 정리
ordered_sigun_df = sigun_df.sort_values('사고번호')

# 구변수 지정
gu = {'남구': 0,
'달서구': 1,
'달성군': 2,
'동구': 3,
'북구': 4,
'서구': 5,
'수성구': 6,
'중구': 7}

ordered_sigun_df['구변수']=ordered_sigun_df['구'].map(gu)


# 시간대 추출
tmp=[]
for x in ordered_sigun_df['사고일시'].values:
    tmp.append(x[-3:-1])

ordered_sigun_df['시간'] = [int(t) for t in tmp]

# 시간대에 일어난 대구 전체 사고량
time_all = ordered_sigun_df.groupby('시간')['시간'].count()

ordered_sigun_df['시간별사고(전체)'] = ordered_sigun_df['시간'].map(time_all)

# 시간대에 일어난 해당 구 사고량
test_df = ordered_sigun_df
listOfDf = []

for reg in test_df['구변수'].unique():
    sub_df = test_df[test_df['구변수']==reg]
    time_sub = sub_df.groupby('시간')['시간'].count()
    sub_df['시간별사고(구)']=sub_df.loc[sub_df['구변수']==reg]['시간'].map(time_sub)
    listOfDf.append(sub_df)
    
last_df = pd.DataFrame(columns=['사고번호','사고일시', '시군구', '구', '구변수', '시간', '시간별사고(전체)', '시간별사고(구)'])

for i in range(0, len(listOfDf[0:])):
    last_df = pd.concat([last_df, listOfDf[0:][i]])
    
last_df = last_df.sort_values('사고번호')
# last_df.to_csv('../데이터/accByTime.csv')

