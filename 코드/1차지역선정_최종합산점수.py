# 연도별 합산 점수를 구하고 최종합산점수를 구하는 코드

# 사용 패키지
import pandas as pd

# 공통 index 설정을 위한 변수 선언 및 index 변수 선언
tra_exp = pd.read_csv('../데이터/1차지역선정_관광소비지수.csv')
ind = tra_exp['지역명']

# 안전지수 변수 선언 후 칼럼, index 수정
safety_score = pd.read_csv('../데이터/지역_연도별_안전지수_minmax2.csv')
safety_score = safety_score.set_index(ind)
safety_score = safety_score.iloc[:,1:5]

# 관광지수 계산을 위한 관광소비지수, 관광지지수, 관광객수 변수 선언
tra_exp = pd.read_csv('../데이터/1차지역선정_관광소비지수.csv')
tra_spot = pd.read_csv('../데이터/1차지역선정_관광지지수.csv') 
traveler = pd.read_csv('../데이터/전처리_시도별관광객수정규화.csv')

# 관광지수 계산, index 수정 후 관광지수 산출
travel = (tra_exp.iloc[:,1:5]*(1/3)) + (tra_spot.iloc[:,1:5]*(1/3)) + (traveler.iloc[:,1:5]*(1/3))
travel = travel.set_index(ind)
travel_score = 1 - travel

# 환경지수 변수 선언 
air = pd.read_csv('../데이터/pollution_final.csv')
park = pd.read_excel('../데이터/area_score.xlsx')
greenhouse = pd.read_csv('../데이터/mm.csv')

# 공통 index 설정
air = air.set_index(ind)
park = park.set_index(ind)
greenhouse = greenhouse.set_index(ind)

# 필요한 칼럼 선택 및 칼럼명 수정
air = air.iloc[:,1:5]
park = park.iloc[:,1:5]
greenhouse = greenhouse.iloc[:,1:5]
greenhouse.columns = ['2018','2019','2020','2021']

# 환경지수 계산
env_score = air*(1/3) + park*(1/3) + greenhouse*(1/3)

# 최종합산점수
total_score = safety_score*0.7 + travel_score*0.1 + env_score*0.2
total_score['합계'] = total_score.sum(axis=1)
total_chart = total_score.sort_values(by= '합계',ascending = False)

# 최종합산점수 결과 csv 파일로 저장
# total_chart.to_csv('../데이터/1차지역선정_최종합산점수.csv', index=True, encoding = 'utf-8')



