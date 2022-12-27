# 2차 지역 선정(구)을 위한 rank 함수 코드

# 사용 패키지
import pandas as pd

# 변수 선언
pop = pd.read_excel('../데이터/구별인구수.xlsx')
intense = pd.read_excel('../데이터/intense.xlsx')
park = pd.read_csv('../데이터/daegu_park.csv')
car = pd.read_csv('../데이터/car.csv')
traveler = pd.read_csv('../데이터/대구방문자수.csv')

# 행, 열 선택 및 정렬 후 index 정리
ind = range(0, 8)
pop = pop.drop([0]).sort_values('구')
pop.index = ind

intense = intense.sort_values('구')
intense.index = ind

car = car.sort_values('시군구')
car.index = ind

# rank 함수를 이용해 구 선정 데이터프레임 만들기
gu_score = pd.DataFrame()
gu_score['구'] = pop['구']
gu_score['인구수'] = pop['총인구수'].rank(method='min')
gu_score['혼잡빈도강도'] = intense['빈도'].rank(method='min')
gu_score['혼잡시간강도'] = intense['시간'].rank(method='min')
gu_score['공원수'] = park['총 공원수'].rank(method='min')
gu_score['공원면적'] = park['총 공원면적'].rank(method='min')
gu_score['차량등록대수'] = car['차량등록대수'].rank(method='min')
gu_score['관광객수'] = traveler['기초지자체 방문자 수'].rank(method='min')
gu_score['sum'] = gu_score.sum(axis=1)

# 2차 지역 선정 점수 csv파일로 저장
# gu_score.to_csv('../데이터/2차지역선정_2차지역선정점수.csv', index=False, encoding='utf-8')
