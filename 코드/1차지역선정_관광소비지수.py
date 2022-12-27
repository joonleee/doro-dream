# 관광지수 산출을 위한 관광소비지수를 구하고 전처리(MinMax)하는 코드

# 사용 패키지
import pandas as pd
from sklearn.preprocessing import minmax_scale

# 시도별 18,19,20,21년도 관광객수 변수 선언
tr_18 = pd.read_csv('../데이터/전처리_18년전국관광객수.csv')
tr_19 = pd.read_csv('../데이터/전처리_19년전국관광객수.csv')
tr_20 = pd.read_csv('../데이터/전처리_20년전국관광객수.csv')
tr_21 = pd.read_csv('../데이터/전처리_21년전국관광객수.csv')

# 시도별 18,19,20,21년도 관광지출액 변수 선언
mo_18 = pd.read_csv('../데이터/전처리_18년전국관광지출액.csv')
mo_19 = pd.read_csv('../데이터/전처리_19년전국관광지출액.csv')
mo_20 = pd.read_csv('../데이터/전처리_20년전국관광지출액.csv')
mo_21 = pd.read_csv('../데이터/전처리_21년전국관광지출액.csv')

# 관광소비지수 산출을 위한 계산
travel_expend = pd.DataFrame()
travel_expend['지역명'] = tr_18['지역명']
travel_expend['2018'] = mo_18['합계']/tr_18['관광객수']
travel_expend['2019'] = mo_19['합계']/tr_19['관광객수']
travel_expend['2020'] = mo_20['합계']/tr_20['관광객수']
travel_expend['2021'] = mo_21['합계']/tr_21['관광객수']

# 정규화한 값으로 관광소비지수 데이터프레임 생성
exp_score = pd.DataFrame()
exp_score['지역명'] = tr_18['지역명']
exp_score['2018'] = minmax_scale(travel_expend['2018'])
exp_score['2019'] = minmax_scale(travel_expend['2019'])
exp_score['2020'] = minmax_scale(travel_expend['2020'])
exp_score['2021'] = minmax_scale(travel_expend['2021'])

# 관광소비지수 csv파일 저장
# exp_score.to_csv('../데이터/1차지역선정_관광소비지수.csv', index=False, encoding = 'utf-8')

