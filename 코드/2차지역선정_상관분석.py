# 2차 지역 선정을 위한 상관분석 코드

# 사용 패키지
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 변수 선언 및 칼럼 정리
cor_df = pd.read_csv('../데이터/2차지역선정_상관분석데이터프레임.csv')
cor_df.columns
cor_df = cor_df.iloc[:,6:18]
cor_df.columns

# 상관분석
corr_result= cor_df.corr(method = 'pearson')

# 상관분석 결과 csv 파일로 저장
# corr_result.to_csv('../데이터/2차지역선정_상관분석결과.csv')

# 상관분석 시각화 히트맵 그리기
plt.rc("font", family = "Malgun Gothic")
sns.set(font="Malgun Gothic", rc={"axes.unicode_minus":False}, style='white')

plt.figure(figsize=(22,19))
sns.heatmap(data = cor_df.corr(), annot=True, fmt = '.2f', linewidths=.5, cmap='Greens', annot_kws={'fontsize' : 25})

