# 시도별 18,19,20,21년도 관광지출액 전처리 코드

# 사용 패키지
import pandas as pd

# 18년도 내국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo18_lo = pd.read_excel('../데이터/money18_lo.xlsx',header=0)
mo18_lo = mo18_lo.iloc[:,[0,2]]
mo18_lo=mo18_lo.drop_duplicates()
mo18_lo.columns=['지역명','지출액']

# 18년도 외국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo18_fo = pd.read_excel('../데이터/money18_fo.xlsx',header=0)
mo18_fo = mo18_fo.iloc[:,[0,2]]
mo18_fo=mo18_fo.drop_duplicates()
mo18_fo.columns=['지역명','지출액']

# 18년 지출액 합
mo18 = pd.merge(left=mo18_lo, right=mo18_fo, on='지역명')
mo18.columns = ['지역명','내국인지출','외국인지출']
mo18['합계'] = mo18['내국인지출'] + mo18['외국인지출']

# 19년도 내국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo19_lo = pd.read_excel('../데이터/money19_lo.xlsx',header=0)
mo19_lo = mo19_lo.iloc[:,[0,2]]
mo19_lo=mo19_lo.drop_duplicates()
mo19_lo.columns=['지역명','지출액']

# 19년도 외국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo19_fo = pd.read_excel('../데이터/money19_fo.xlsx',header=0)
mo19_fo = mo19_fo.iloc[:,[0,2]]
mo19_fo=mo19_fo.drop_duplicates()
mo19_fo.columns=['지역명','지출액']

# 19년 지출액 합
mo19 = pd.merge(left=mo19_lo, right=mo19_fo, on='지역명')
mo19.columns = ['지역명','내국인지출','외국인지출']
mo19['합계'] = mo19['내국인지출'] + mo19['외국인지출']

# 20년도 내국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo20_lo = pd.read_excel('../데이터/money20_lo.xlsx',header=0)
mo20_lo = mo20_lo.iloc[:,[0,2]]
mo20_lo=mo20_lo.drop_duplicates()
mo20_lo.columns=['지역명','지출액']

# 20년도 외국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo20_fo = pd.read_excel('../데이터/money20_fo.xlsx',header=0)
mo20_fo = mo20_fo.iloc[:,[0,2]]
mo20_fo=mo20_fo.drop_duplicates()
mo20_fo.columns=['지역명','지출액']

# 20년 지출액 합
mo20 = pd.merge(left=mo20_lo, right=mo20_fo, on='지역명')
mo20.columns = ['지역명','내국인지출','외국인지출']
mo20['합계'] = mo20['내국인지출'] + mo20['외국인지출']

# 21년도 내국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo21_lo = pd.read_excel('../데이터/money21_lo.xlsx',header=0)
mo21_lo = mo21_lo.iloc[:,[0,2]]
mo21_lo=mo21_lo.drop_duplicates()
mo21_lo.columns=['지역명','지출액']

# 21년도 외국인 관광지출액 변수 선언, 필요한 칼럼 선택 후 중복행 제거 후 칼럼명 설정
mo21_fo = pd.read_excel('../데이터/money21_fo.xlsx',header=0)
mo21_fo = mo21_fo.iloc[:,[0,2]]
mo21_fo=mo21_fo.drop_duplicates()
mo21_fo.columns=['지역명','지출액']

# 21년 지출액 합
mo21 = pd.merge(left=mo21_lo, right=mo21_fo, on='지역명')
mo21.columns = ['지역명','내국인지출','외국인지출']
mo21['합계'] = mo21['내국인지출'] + mo21['외국인지출']

# 지수 산출시 사용하기 위해 연도별 관광지출액을 csv파일로 저장
# mo18.to_csv('../데이터/전처리_18년전국관광지출액.csv', index=False, encoding = 'utf-8')
# mo19.to_csv('../데이터/전처리_19년전국관광지출액.csv', index=False, encoding = 'utf-8')
# mo20.to_csv('../데이터/전처리_20년전국관광지출액.csv', index=False, encoding = 'utf-8')
# mo21.to_csv('../데이터/전처리_21년전국관광지출액.csv', index=False, encoding = 'utf-8')
