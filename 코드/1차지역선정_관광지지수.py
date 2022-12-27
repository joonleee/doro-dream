# 관광지수 산출을 위한 관광지 지수를 구하고 전처리(MinMax)하는 코드

# 사용 패키지
import pandas as pd
from sklearn.preprocessing import minmax_scale

# 시도별 관광지개수, 인구수 데이터 변수 선언
pop = pd.read_csv('../데이터/전처리_행정구역별인구수.csv')
tra_num = pd.read_csv('../데이터/전처리_시도별관광지개수.csv')

# 관광지지수 산출을 위한 계산
travel_spot = pd.DataFrame()
travel_spot['지역명'] = tra_num['지역명']
travel_spot['2018'] = tra_num['관광지개수']/pop['2018']
travel_spot['2019'] = tra_num['관광지개수']/pop['2019']
travel_spot['2020'] = tra_num['관광지개수']/pop['2020']
travel_spot['2021'] = tra_num['관광지개수']/pop['2021']

# 정규화한 값으로 관광소비지수 데이터프레임 생성
spot_score = pd.DataFrame()
spot_score['지역명'] = tra_num['지역명']
spot_score['2018'] = minmax_scale(travel_spot['2018'])
spot_score['2019'] = minmax_scale(travel_spot['2019'])
spot_score['2020'] = minmax_scale(travel_spot['2020'])
spot_score['2021'] = minmax_scale(travel_spot['2021'])

# 관광소비지수 csv파일 저장
# spot_score.to_csv('../데이터/1차지역선정_관광지지수.csv', index=False, encoding = 'utf-8')
