# 사용 패키지
import pandas as pd 
import numpy as np


ozone2018 = pd.read_csv('../데이터/ozone_month_city2018.csv')
oz_2018 = ozone2018.iloc[:, 2:14]
oz_2018m = oz_2018.mean(axis=1, numeric_only=False)

ozone2019 = pd.read_csv('../데이터/ozone_month_city2019.csv')
oz_2019 = ozone2019.iloc[:, 2:14]
oz_2019m = oz_2019.mean(axis=1, numeric_only=False)

ozone2020 = pd.read_csv('../데이터/ozone_month_city2020.csv')
ozone2020.info()
oz_2020 = ozone2020.iloc[:, 2:14]
oz_2020m = oz_2020.mean(axis=1, numeric_only=False)

ozone2021 = pd.read_csv('../데이터/ozone_month_city2021.csv')
ozone2021.info()
oz_2021 = ozone2018.iloc[:, 2:12]
oz_2021m = oz_2021.mean(axis=1, numeric_only=False)


PM252018 = pd.read_csv('../데이터/PM2.5_month_city2018.csv')
PM25_2018 = PM252018.iloc[:, 2:14]
PM25_2018m = PM25_2018.mean(axis=1, numeric_only=False)

PM252019 = pd.read_csv('../데이터/PM2.5_month_city2019.csv')
PM25_2019 = PM252019.iloc[:, 2:14]
PM25_2019m = PM25_2019.mean(axis=1, numeric_only=False)

PM252020 = pd.read_csv('../데이터/PM2.5_month_city2020.csv')
PM25_2020 = PM252020.iloc[:, 2:14]
PM25_2020m = PM25_2020.mean(axis=1, numeric_only=False)

PM252021 = pd.read_csv('../데이터/PM2.5_month_city2021.csv')
PM25_2021 = PM252021.iloc[:, 2:12]
PM25_2021m = PM25_2021.mean(axis=1, numeric_only=False)

PM102018 = pd.read_csv('../데이터/PM10_month_city2018.csv')
PM10_2018 = PM102018.iloc[:, 2:14]
PM10_2018m = PM10_2018.mean(axis=1, numeric_only=False)

PM102019 = pd.read_csv('../데이터/PM10_month_city2019.csv')
PM10_2019 = PM102019.iloc[:, 2:14]
PM10_2019m = PM10_2019.mean(axis=1, numeric_only=False)

PM102020 = pd.read_csv('../데이터/PM10_month_city2020.csv')
PM10_2020 = PM102020.iloc[:, 2:14]
PM10_2020m = PM10_2020.mean(axis=1, numeric_only=False)

PM102021 = pd.read_csv('../데이터/PM10_month_city2021.csv')
PM10_2021 = PM102021.iloc[:, 2:12]
PM10_2021m = PM10_2021.mean(axis=1, numeric_only=False)