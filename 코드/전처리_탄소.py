# 사용 패키지
import os
import pandas as pd
from sklearn.preprocessing import minmax_scale

# 받아온 데이터
cm_2018_df = pd.read_csv('../데이터/CM2018.csv')
cm_2019_df = pd.read_csv('../데이터/CM2019.csv')
cm_2020_df = pd.read_csv('../데이터/CM2020.csv')
cm_2021_df = pd.read_csv('../데이터/CM2021.csv')

nd_2018_df = pd.read_csv('../데이터/ND2018.csv')
nd_2019_df = pd.read_csv('../데이터/ND2019.csv')
nd_2020_df = pd.read_csv('../데이터/ND2020.csv')
nd_2021_df = pd.read_csv('../데이터/ND2021.csv')

sd_2018_df = pd.read_csv('../데이터/SD2018.csv')
sd_2019_df = pd.read_csv('../데이터/SD2019.csv')
sd_2020_df = pd.read_csv('../데이터/SD2020.csv')
sd_2021_df = pd.read_csv('../데이터/SD2021.csv')



#CM
#2018
newcm2018 = cm_2018_df.loc[(cm_2018_df["구분(2)"].str.contains("특별시")) | (cm_2018_df["구분(2)"].str.contains("세종")) | (cm_2018_df["구분(2)"].str.contains("광역시"))  |(cm_2018_df["구분(2)"] == "도평균")]
cm_month2018 = newcm2018.iloc[:, 2:14]
cm_month2018 = cm_month2018.astype(float)
cm2018 = cm_month2018.mean(axis=1, numeric_only=False)

#2019
newcm2019 = cm_2019_df.loc[(cm_2019_df["구분(2)"].str.contains("특별시")) | (cm_2019_df["구분(2)"].str.contains("세종")) | (cm_2019_df["구분(2)"].str.contains("광역시"))  |(cm_2019_df["구분(2)"] == "도평균")]
cm_month2019 = newcm2019.iloc[:,2:14]
cm_month2019 = cm_month2019.astype(float)
cm2019 = cm_month2019.mean(axis=1, numeric_only=False)

#2020
newcm2020 = cm_2020_df.loc[(cm_2020_df["구분(2)"].str.contains("특별시")) | (cm_2020_df["구분(2)"].str.contains("세종")) | (cm_2020_df["구분(2)"].str.contains("광역시"))  |(cm_2020_df["구분(2)"] == "도평균")]
cm_month2020 = newcm2020.iloc[:,2:14]
cm_month2020 = cm_month2020.astype(float)
cm2020 = cm_month2020.mean(axis=1, numeric_only=False)

#2021
newcm2021 = cm_2021_df.loc[(cm_2021_df["구분(2)"].str.contains("특별시")) | (cm_2021_df["구분(2)"].str.contains("세종")) | (cm_2021_df["구분(2)"].str.contains("광역시"))  |(cm_2021_df["구분(2)"] == "도평균")]
cm_month2021 = newcm2021.iloc[:,2:12]
cm_month2021 = cm_month2021.astype(float)
cm2021 = cm_month2021.mean(axis=1, numeric_only=False)

#ND
#2018
newnd2018 = nd_2018_df.loc[(nd_2018_df["구분(2)"].str.contains("특별시")) | (nd_2018_df["구분(2)"].str.contains("세종")) | (nd_2018_df["구분(2)"].str.contains("광역시"))  |(nd_2018_df["구분(2)"] == "도평균")]
nd_month2018 = newnd2018.iloc[:, 2:14]
nd_month2018 = nd_month2018.astype(float)
nd2018 = nd_month2018.mean(axis=1, numeric_only=False)

#2019
newnd2019 = nd_2019_df.loc[(nd_2019_df["구분(2)"].str.contains("특별시")) | (nd_2019_df["구분(2)"].str.contains("세종")) | (nd_2019_df["구분(2)"].str.contains("광역시"))  |(nd_2019_df["구분(2)"] == "도평균")]
nd_month2019 = newnd2019.iloc[:, 2:14]
nd_month2019 = nd_month2019.astype(float)
nd2019 = nd_month2019.mean(axis=1, numeric_only=False)

#2020
newnd2020 = nd_2020_df.loc[(nd_2020_df["구분(2)"].str.contains("특별시")) | (nd_2020_df["구분(2)"].str.contains("세종")) | (nd_2020_df["구분(2)"].str.contains("광역시"))  |(nd_2020_df["구분(2)"] == "도평균")]
nd_month2020 = newnd2020.iloc[:, 2:14]
nd_month2020 = nd_month2020.astype(float)
nd2020 = nd_month2020.mean(axis=1, numeric_only=False)

#2021
newnd2021 = nd_2021_df.loc[(nd_2021_df["구분(2)"].str.contains("특별시")) | (nd_2021_df["구분(2)"].str.contains("세종")) | (nd_2021_df["구분(2)"].str.contains("광역시"))  |(nd_2021_df["구분(2)"] == "도평균")]
nd_month2021 = newnd2021.iloc[:,2:12]
nd_month2021 = nd_month2021.astype(float)
nd2021 = nd_month2021.mean(axis=1, numeric_only=False)


#SD
#2018
newsd2018 = sd_2018_df.loc[(sd_2018_df["구분(2)"].str.contains("특별시")) | (sd_2018_df["구분(2)"].str.contains("세종")) | (sd_2018_df["구분(2)"].str.contains("광역시"))  |(sd_2018_df["구분(2)"] == "도평균")]
sd_month2018 = newsd2018.iloc[:, 2:14]
sd_month2018 = sd_month2018.astype(float)
sd2018 = sd_month2018.mean(axis=1, numeric_only=False)

#2019
newsd2019 = sd_2019_df.loc[(sd_2019_df["구분(2)"].str.contains("특별시")) | (sd_2019_df["구분(2)"].str.contains("세종")) | (sd_2019_df["구분(2)"].str.contains("광역시"))  |(sd_2019_df["구분(2)"] == "도평균")]
sd_month2019 = newsd2019.iloc[:, 2:14]
sd_month2019 = sd_month2019.astype(float)
sd2019 = sd_month2019.mean(axis=1, numeric_only=False)

#2020
newsd2020 = sd_2020_df.loc[(sd_2020_df["구분(2)"].str.contains("특별시")) | (sd_2020_df["구분(2)"].str.contains("세종")) | (sd_2020_df["구분(2)"].str.contains("광역시"))  |(sd_2020_df["구분(2)"] == "도평균")]
sd_month2020 = newsd2020.iloc[:, 2:14]
sd_month2020 = sd_month2020.astype(float)
sd2020 = sd_month2020.mean(axis=1, numeric_only=False)

#2021
newsd2021 = sd_2021_df.loc[(sd_2021_df["구분(2)"].str.contains("특별시")) | (sd_2021_df["구분(2)"].str.contains("세종")) | (sd_2021_df["구분(2)"].str.contains("광역시"))  |(sd_2021_df["구분(2)"] == "도평균")]
sd_month2021 = newsd2021.iloc[:,2:12]
sd_month2021 = sd_month2021.astype(float)
sd2021 = sd_month2021.mean(axis=1, numeric_only=False)



# average table
table={'도시명':['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']}
pollution = pd.DataFrame(table)

#CM
pollution['CM2018'] = cm2018.values.tolist()
pollution['CM2019'] = cm2019.values.tolist()
pollution['CM2020'] = cm2020.values.tolist()
pollution['CM2021'] = cm2021.values.tolist()
#ND
pollution['ND2018'] = nd2018.values.tolist()
pollution['ND2019'] = nd2019.values.tolist()
pollution['ND2020'] = nd2020.values.tolist()
pollution['ND2021'] = nd2021.values.tolist()
#SD
pollution['SD2018'] = sd2018.values.tolist()
pollution['SD2019'] = sd2019.values.tolist()
pollution['SD2020'] = sd2020.values.tolist()
pollution['SD2021'] = sd2021.values.tolist()

# pollution.to_csv('../데이터/pollution_tot.csv')



#min-max
min_max_scaler = MinMaxScaler()
#CM
minmax_cm2018 = minmax_scale(cm2018)
minmax_cm2019 = minmax_scale(cm2019)
minmax_cm2020 = minmax_scale(cm2020)
minmax_cm2021 = minmax_scale(cm2021)
#ND
minmax_nd2018 = minmax_scale(nd2018)
minmax_nd2019 = minmax_scale(nd2019)
minmax_nd2020 = minmax_scale(nd2020)
minmax_nd2021 = minmax_scale(nd2021)
#SD
minmax_sd2018 = minmax_scale(sd2018)
minmax_sd2019 = minmax_scale(sd2019)
minmax_sd2020 = minmax_scale(sd2020)
minmax_sd2021 = minmax_scale(sd2021)


# pollution_mm data frame
#CM
pollution_mm = pd.DataFrame(table)
pollution_mm['cm2018_mm'] = minmax_cm2018
pollution_mm['cm2019_mm'] = minmax_cm2019
pollution_mm['cm2020_mm'] = minmax_cm2020
pollution_mm['cm2021_mm'] = minmax_cm2021
#ND
pollution_mm['nd2018_mm'] = minmax_nd2018
pollution_mm['nd2019_mm'] = minmax_nd2019
pollution_mm['nd2020_mm'] = minmax_nd2020
pollution_mm['nd2021_mm'] = minmax_nd2021
#SD
pollution_mm['sd2018_mm'] = minmax_sd2018
pollution_mm['sd2019_mm'] = minmax_sd2019
pollution_mm['sd2020_mm'] = minmax_sd2020
pollution_mm['sd2021_mm'] = minmax_sd2021

# pollution_mm.to_csv('../데이터/pollution_minmax.csv')