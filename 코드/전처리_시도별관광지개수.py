# 전국 시도별 관광지 개수 코드

# 사용 패키지
import pandas as pd

# 전국 관광지개수 데이터 불러오기
tra_num = pd.read_excel('../데이터/지역별관광지개수.xlsx')

# 행정구역 순으로 정렬
tra_num = tra_num.sort_values('지역명')

# 전국관광지개수 csv파일 저장
# tra_num.to_csv('../데이터/전처리_시도별관광지개수.csv', index=False, encoding = 'utf-8')

