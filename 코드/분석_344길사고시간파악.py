# 사용 패키지
import pandas as pd

# 사용 변수
sago = pd.read_csv('../데이터/전처리_21년대구사고지역시간좌표.csv')

# 실제 달구벌대로344길에서 발생한 보행자사고 좌표 9개
gil9=pd.read_csv('../데이터/344gil.txt')

# 불필요한 정보 제거
sago = sago[sago['구']=='달서구']
sago = sago[['시간','lat','long', '사고번호', '사고일시']]

# 달구벌대로344길에서 유효한 사고 좌표로 사고가 난 시간대 파악
time=[]
for line in sago.values:
    for gil in gil9.values:
        if gil[0] == line[1]:
            if line[0] not in time:
                time.append(line[0])
            
time.sort()

