# 상관분석을 하기 위한 데이터프레임을 만드는 코드

# 사용 패키지
import pandas as pd

# 대구 보행자 교통사고 ID 데이터 불러오기
id21 = pd.read_csv('../데이터/대구보행자교통사고ID.csv')
id21.columns
# ['사고번호', '사고일시', '사고장소', '사고시간', '구', '구변수']

# 대구 보행자 교통사고 ID 데이터(구별시간별사고량 포함) 불러오기
acci = pd.read_csv('../데이터/accByTime.csv')
acci.columns
# ['Unnamed: 0', '사고번호', '사고일시', '시군구', '군', '군변수', '시간', '시간별사고(전체)', '시간별사고(구)']

# 대구 보행자 교통사고 ID 데이터(차량등록대수, 구별공원총면적, 구별공원개수 포함) 불러오기
areacar = pd.read_csv('../데이터/areacar.csv')
areacar.columns
# ['Unnamed: 0', '사고번호', '사고일시', '시군구', '군', '군변수', '시간', '차량등록대수', '구공원총면적/구면적', '구공원총면적', '구공원개수']

# 구별 관광지 개수 변수
traplace = pd.read_excel('../데이터/구별관광지개수.xlsx') 

# 구별 관광객 수 변수
traveler = pd.read_csv('../데이터/대구방문자수.csv')

# 대구추정교통량 데이터 변수 선언 및 행, 칼럼 선택
traf_vol = pd.read_csv('../데이터/추정교통량.csv')
traf_vol = traf_vol.iloc[:8, :26]

# 구별 보행자 교통사고량 데이터
acd = pd.read_excel('../데이터/구별보행자교통사고량.xlsx')

# 구별 인구수 데이터 로드 후 정렬
pop = pd.read_excel('../데이터/구별인구수.xlsx')
pop = pop.drop([0])
pop.sort_values('구', inplace=True)

# 혼잡빈도,시간강도 데이터 로드 후 정렬
inten = pd.read_excel('../데이터/intense.xlsx')
inten = inten.sort_values('구')

# 교통사고 ID데이터 변수(id21)에 구별시간별사고량, 차량등록대수, 구별공원총면적, 구별공원개수 추가
id21['구별시간별사고량'] = acci['시간별사고(구)']
id21['차량등록대수'] = areacar['차량등록대수']
id21['구별공원총면적'] = areacar['구공원총면적']
id21['구별공원개수'] = areacar['구공원개수']

# 관광지 개수 칼럼 추가
id21['구별관광지개수'] = 0

for i in range(0,2116) :
    
    if id21.iloc[i,5] == 0:
        id21.iloc[i,10] = 7
        
    elif id21.iloc[i,5] == 1:
        id21.iloc[i,10] = 4
        
    elif id21.iloc[i,5] == 2:
        id21.iloc[i,10] = 15
         
    elif id21.iloc[i,5] == 3:
        id21.iloc[i,10] = 7        
           
    elif id21.iloc[i,5] == 4:
        id21.iloc[i,10] = 2 

    elif id21.iloc[i,5] == 5:
        id21.iloc[i,10] = 3 

    elif id21.iloc[i,5] == 6:
        id21.iloc[i,10] = 5 
        
    elif id21.iloc[i,5] == 7:
        id21.iloc[i,10] = 10 
        
    else :
        print('error')
        
# for문 결과 점검
id_group = id21.groupby(['구변수','구별관광지개수']) 
id_group.size()        
        
# 구전체추정교통량 칼럼 추가
id21['구전체추정교통량'] = 0

for i in range(0,2116) :
    if id21.iloc[i,5] == 0: # 남구
        id21.iloc[i,11] = 11106
        
    elif id21.iloc[i,5] == 1:
        id21.iloc[i,11] = 8375
        
    elif id21.iloc[i,5] == 2:
        id21.iloc[i,11] = 4170
         
    elif id21.iloc[i,5] == 3:
        id21.iloc[i,11] = 8295        
           
    elif id21.iloc[i,5] == 4:
        id21.iloc[i,11] = 10236

    elif id21.iloc[i,5] == 5:
        id21.iloc[i,11] = 13536 

    elif id21.iloc[i,5] == 6:
        id21.iloc[i,11] = 9149
        
    elif id21.iloc[i,5] == 7:
        id21.iloc[i,11] = 11595 
        
    else :
        print('error')     

# for문 결과 점검
id_group = id21.groupby(['구변수','구전체추정교통량']) 
id_group.size()  

# 구별시간대별추정교통량 칼럼 추가
id21['구별시간대별추정교통량'] = 0

for i in range(0,2116) : # 열   
    
    for j in range(0,24) :
    
        if id21.iloc[i,3] == j : # 시간 = j시
           
           a = j + 2
        
           if id21.iloc[i,5] == 0: # 남구
                    t = traf_vol.iloc[0,a]
                    id21.iloc[i,12] = t
                    
           elif id21.iloc[i,5] == 1: # 달서구
                    t = traf_vol.iloc[1,a]
                    id21.iloc[i,12] = t
                   
           elif id21.iloc[i,5] == 2: # 달성군
                    t = traf_vol.iloc[2,a]
                    id21.iloc[i,12] = t
                     
           elif id21.iloc[i,5] == 3: # 동구
                    t = traf_vol.iloc[3,a]
                    id21.iloc[i,12] = t        
                       
           elif id21.iloc[i,5] == 4: # 북구
                    t = traf_vol.iloc[4,a]
                    id21.iloc[i,12] = t 
            
           elif id21.iloc[i,5] == 5: # 서구
                    t = traf_vol.iloc[5,a]
                    id21.iloc[i,12] = t 
            
           elif id21.iloc[i,5] == 6: # 수성구
                    t = traf_vol.iloc[6,a]
                    id21.iloc[i,12] = t 
                    
           elif id21.iloc[i,5] == 7: # 중구
                    t = traf_vol.iloc[7,a]
                    id21.iloc[i,12] = t  
                    
           else :
                    print('error')
                    
# 구별 보행자 교통사고량 칼럼 추가
id21['구별보행자교통사고량'] = 0

for i in range(0,2116) :
    
    if id21.iloc[i,5] == 0:
        id21.iloc[i,13] = 156
        
    elif id21.iloc[i,5] == 1:
        id21.iloc[i,13] = 550
        
    elif id21.iloc[i,5] == 2:
        id21.iloc[i,13] = 113
         
    elif id21.iloc[i,5] == 3:
        id21.iloc[i,13] = 259      
           
    elif id21.iloc[i,5] == 4:
        id21.iloc[i,13] = 328 

    elif id21.iloc[i,5] == 5:
        id21.iloc[i,13] = 187 

    elif id21.iloc[i,5] == 6:
        id21.iloc[i,13] = 366 
        
    elif id21.iloc[i,5] == 7:
        id21.iloc[i,13] = 157 
        
    else :
        print('error')
        
# 구별 인구수 칼럼 추가
id21['구별인구수'] = 0

for i in range(0,2116) :

    if id21.iloc[i,5] == 0:
        id21.iloc[i,14] = pop.iloc[0,1]
        
    elif id21.iloc[i,5] == 1:
        id21.iloc[i,14] = pop.iloc[1,1]
        
    elif id21.iloc[i,5] == 2:
        id21.iloc[i,14] = pop.iloc[2,1]
         
    elif id21.iloc[i,5] == 3:
        id21.iloc[i,14] = pop.iloc[3,1]
           
    elif id21.iloc[i,5] == 4:
        id21.iloc[i,14] = pop.iloc[4,1] 

    elif id21.iloc[i,5] == 5:
        id21.iloc[i,14] = pop.iloc[5,1]

    elif id21.iloc[i,5] == 6:
        id21.iloc[i,14] = pop.iloc[6,1]
        
    elif id21.iloc[i,5] == 7:
        id21.iloc[i,14] = pop.iloc[7,1]
        
    else :
        print('error')

# 구별 혼잡빈도강도 칼럼 추가
id21['구별혼잡빈도강도'] = 0

for i in range(0,2116) :

    if id21.iloc[i,5] == 0:
        id21.iloc[i,15] = inten.iloc[0,1]
        
    elif id21.iloc[i,5] == 1:
        id21.iloc[i,15] = inten.iloc[1,1]
        
    elif id21.iloc[i,5] == 2:
        id21.iloc[i,15] = inten.iloc[2,1]
         
    elif id21.iloc[i,5] == 3:
        id21.iloc[i,15] = inten.iloc[3,1]
           
    elif id21.iloc[i,5] == 4:
        id21.iloc[i,15] = inten.iloc[4,1] 

    elif id21.iloc[i,5] == 5:
        id21.iloc[i,15] = inten.iloc[5,1]

    elif id21.iloc[i,5] == 6:
        id21.iloc[i,15] = inten.iloc[6,1]
        
    elif id21.iloc[i,5] == 7:
        id21.iloc[i,15] = inten.iloc[7,1]
        
    else :
        print('error')

# 구별 혼잡시간강도 칼럼 추가
id21['구별혼잡시간강도'] = 0

for i in range(0,2116) :

    if id21.iloc[i,5] == 0:
        id21.iloc[i,16] = inten.iloc[0,2]
        
    elif id21.iloc[i,5] == 1:
        id21.iloc[i,16] = inten.iloc[1,2]
        
    elif id21.iloc[i,5] == 2:
        id21.iloc[i,16] = inten.iloc[2,2]
         
    elif id21.iloc[i,5] == 3:
        id21.iloc[i,16] = inten.iloc[3,2]
           
    elif id21.iloc[i,5] == 4:
        id21.iloc[i,16] = inten.iloc[4,2] 

    elif id21.iloc[i,5] == 5:
        id21.iloc[i,16] = inten.iloc[5,2]

    elif id21.iloc[i,5] == 6:
        id21.iloc[i,16] = inten.iloc[6,2]
        
    elif id21.iloc[i,5] == 7:
        id21.iloc[i,16] = inten.iloc[7,2]
        
    else :
        print('error')

# 구별 관광객 수 칼럼 추가
id21['구별관광객수'] = 0

for i in range(0,2116) :

    if id21.iloc[i,5] == 0:
        id21.iloc[i,17] = 51136826
        
    elif id21.iloc[i,5] == 1:
        id21.iloc[i,17] = 155410336
        
    elif id21.iloc[i,5] == 2:
        id21.iloc[i,17] = 70853448
         
    elif id21.iloc[i,5] == 3:
        id21.iloc[i,17] = 110897532      
           
    elif id21.iloc[i,5] == 4:
        id21.iloc[i,17] = 132444489 

    elif id21.iloc[i,5] == 5:
        id21.iloc[i,17] = 41488544 

    elif id21.iloc[i,5] == 6:
        id21.iloc[i,17] = 130910791 
        
    elif id21.iloc[i,5] == 7:
        id21.iloc[i,17] = 77419220 
        
    else :
        print('error')
        
# 데이터프레임 csv 파일로 저장
# id21.to_csv('../데이터/2차지역선정_상관분석데이터프레임.csv', index=False, encoding='utf-8')







