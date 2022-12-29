# 18~21년 데이터 병합, 온실가스지수

# 사용 패키지
import numpy as np
import pandas as pd
from sklearn.preprocessing import minmax_scale

#2018년도
df1 = pd.read_csv('../데이터/Greenhouse_2018.csv', encoding='euc-kr')

# 불필요 칼럼 삭제
df1 = df1.drop(['년도'], axis = 1) #열삭제

test = df1[['이산화탄소 (CO2)', '메탄 (CH4)', '아산화질소(N2O)']]

# sum 열에 합 입력
a = test.sum(axis=1).values
test['sum'] = a

# 파일 저장
# test.to_csv("../데이터/Sum_2018.csv",  index = False)


#2019년도
df2 = pd.read_csv('../데이터/Greenhouse_2019.csv', encoding='euc-kr')

# 불필요 칼럼 삭제
df2 = df2.drop(['년도'], axis = 1)

test = df2[['이산화탄소 (CO2)', '메탄 (CH4)', '아산화질소(N2O)']]

# sum 열에 합 입력
a = test.sum(axis=1).values
test['sum'] = a

# 파일 저장
# test.to_csv("Sum_2019.csv",  index = False)

#2020년도
df3 = pd.read_csv('../데이터/Greenhouse_2020.csv', encoding='euc-kr')

# 불필요 칼럼 삭제
df3 = df3.drop(['년도'], axis = 1)

test = df3[['이산화탄소 (CO2)', '메탄 (CH4)', '아산화질소(N2O)']]

# sum 열에 합 입력
a = test.sum(axis=1).values
test['sum'] = a

# 파일 저장
# test.to_csv("Sum_2020.csv",  index = False)

#2021년도
d4['2021'] = 0 #결측치 처리


#정규화 
d1 = pd.read_csv('../데이터/Sum_2018.csv', encoding='utf-8')
d2 = pd.read_csv('../데이터/Sum_2019.csv', encoding='utf-8')
d3 = pd.read_csv('../데이터/Sum_2020.csv', encoding='utf-8')

d1['2018_mm'] = minmax_scale(d1['sum'])
d2['2019_mm'] = minmax_scale(d2['sum'])
d3['2020_mm'] = minmax_scale(d3['sum'])

# 데이터 저장
# d1.to_csv("Greenhouse_mm2018.csv",  index = False)
# d2.to_csv("Greenhouse_mm2019.csv",  index = False)
# d3.to_csv("Greenhouse_mm2020.csv",  index = False)


#데이터 프레임 합치기

d1 = pd.read_csv('../데이터/Greenhouse_mm2018.csv', encoding='utf-8')
d2 = pd.read_csv('../데이터/Greenhouse_mm2019.csv', encoding='utf-8')
d3 = pd.read_csv('../데이터/Greenhouse_mm2020.csv', encoding='utf-8')

d1 = d1.drop(['이산화탄소 (CO2)','메탄 (CH4)','아산화질소(N2O)','sum'], axis = 1)
d2 = d2.drop(['이산화탄소 (CO2)','메탄 (CH4)','아산화질소(N2O)','sum'], axis = 1)
d3 = d3.drop(['이산화탄소 (CO2)','메탄 (CH4)','아산화질소(N2O)','sum'], axis = 1)

d4 = pd.concat([d1, d2, d3],axis = 1)

#지역명 추가                
d5 = d4.insert(1,'region',['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주도'])

#저장
# d4.to_csv("mm.csv",  index = False) #저장
