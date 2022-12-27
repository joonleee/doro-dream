# 시도별 18,19,20,21년도 관광객수 전처리(MinMax Scale) 코드

# 사용 패키지
import pandas as pd
from sklearn.preprocessing import minmax_scale

# 변수 선언
tr18 = pd.read_excel('../데이터/tr18.xlsx',header=0)
tr19 = pd.read_excel('../데이터/tr19.xlsx',header=0)
tr20 = pd.read_excel('../데이터/tr20.xlsx',header=0)
tr21 = pd.read_excel('../데이터/tr21.xlsx',header=0)

# 필요한 칼럼 선택
tr18 = tr18.iloc[:,[0,2]]
tr19 = tr19.iloc[:,[0,2]]
tr20 = tr20.iloc[:,[0,2]]
tr21 = tr21.iloc[:,[0,2]]

# 중복행 제거 후 칼럼명 설정
tr_18 = tr18.drop_duplicates()
tr_18.columns=['지역명','관광객수']

tr_19 = tr19.drop_duplicates()
tr_19.columns=['지역명','관광객수']

tr_20 = tr20.drop_duplicates()
tr_20.columns=['지역명','관광객수']

tr_21 = tr21.drop_duplicates()
tr_21.columns=['지역명','관광객수']

# 지수 산출시 사용하기 위해 연도별 관광객 수를 csv파일로 저장
# tr_18.to_csv('../데이터/전처리_18년전국관광객수.csv', index=False, encoding = 'utf-8')
# tr_19.to_csv('../데이터/전처리_19년전국관광객수.csv', index=False, encoding = 'utf-8')
# tr_20.to_csv('../데이터/전처리_20년전국관광객수.csv', index=False, encoding = 'utf-8')
# tr_21.to_csv('../데이터/전처리_21년전국관광객수.csv', index=False, encoding = 'utf-8')

# 연도별 관광객수를 정규화한 값으로 데이터프레임 생성
tr_score=pd.DataFrame()
tr_score['지역명'] = tr_21['지역명']
tr_score['2018'] = minmax_scale(tr_18.iloc[:,1])
tr_score['2019'] = minmax_scale(tr_19.iloc[:,1])
tr_score['2020'] = minmax_scale(tr_20.iloc[:,1])
tr_score['2021'] = minmax_scale(tr_21.iloc[:,1])

# 전처리 결과를 csv파일로 저장
# tr_score.to_csv('../데이터/전처리_시도별관광객수정규화.csv', index=False, encoding = 'utf-8')






