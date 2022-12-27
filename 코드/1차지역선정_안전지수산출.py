# 사용 패키지
import pandas as pd
from sklearn.preprocessing import minmax_scale

# 사용 변수
region = ['강원도',
'경기도',
'경상남도',
'경상북도',
'광주광역시',
'대구광역시',
'대전광역시',
'부산광역시',
'서울특별시',
'세종특별자치시',
'울산광역시',
'인천광역시',
'전라남도',
'전라북도',
'제주도',
'충청남도',
'충청북도']

year=[18, 19, 20, 21]
file_accident = {}
score_df = pd.DataFrame(columns=['2018', '2019', '2020', '2021'])
minmax_df = pd.DataFrame(columns=['2018', '2019', '2020', '2021'])

# 지역별 사망자수, 부상자수, 총인구 추출하여 score_df에 저장
for reg in region:
    tmp=[]
    for yr in year:
        df = pd.read_csv(f'../데이터/교통사고정보_보행자사고/연별/{reg}_all.csv')
        df =  df[(df['사고일시'] >= f'20{yr}-01-01') & (df['사고일시'] < f'20{yr+1}-01-01')]
        death = sum(df['사망자수'])
        injury = sum(df['중상자수'])+sum(df['경상자수'])+sum(df['부상신고자수'])
#         print(reg, yr, death, injury)
        pop = pd.read_csv(f'../데이터/행정안전부_주민등록인구통계/201712_202112_주민등록인구및세대현황_연간_{reg}.csv')
        pop = pop[f'20{yr}년_총인구수'].str.replace(',','').astype(int)
        tot_pop = pop[0]
        
        tp_score = (((death*4) + (injury*1))/tot_pop)*100000
        tmp.append(tp_score)
    score_df.loc[reg] = tmp

# minmax 후 지역별 연도별 안전지수 저장
for yr in year:
    minmax_df[f'20{yr}'] = minmax_scale(score_df[f'20{yr}'])
minmax_df.index = region

# minmax_df.to_csv('../데이터/지역_연도별_안전지수_minmax.csv')

