# doro-dream

## 배경

교통안전공단에 따르면, 2021년 대한민국에서 3만 5천건 정도의 보행자 사고가 발생했고, 그 중 1018명이 사망했다. 적지 않은 수치다.

교통사고는 언제 어디서든 일어날 수 있고, 우리에게도 일어날 수 있는 일이다. 

따라서 우리는 보행자의 안전한 보행을 돕기 위해 도로 드림 프로젝트를 진행하였다.

> 보행자 사고 다발 구역에 차량 진입을 제한하여 보행자 교통사고를 감소시킴과 동시에, 해당 도로에 나무를 심고, 벤치를 설치하는 등 하나의 문화공간이 될 수 있도록 도심 속 쉼터를 만드는 프로젝트

---

## 목적

다음과 같은 기대 효과를 얻고자 분석을 진행하였다.

- 첫째, 해당 도로를 보행자를 위한 도로로 만듦으로써 보행자 교통사고 감소.
- 둘째, 대중교통 이용률이 증가하고, 도로에 차 대신 나무를 심음으로써 도시 환경 개선.
- 셋째, 해당 도로가 하나의 특색있는 거리가 된다면, 많은 사람들이 찾을 것이고, 자연스레 지역 경제 활성화를 기대.
----
## 사용 데이터

- 안전 데이터
    - 보행자 교통사고 데이터 ([교통사고정보 개방 시스템](http://taas.koroad.or.kr/web/shp/adi/initOpenApi.do?menuId=WEB_KMP_TAI_TOS))
    - 자동차 등록 현황 (각 지자체에 받아옴)
    - 시도별 추정 교통량 데이터 ([View-T](https://viewt.ktdb.go.kr/cong/map/page.do))
    - 교통 혼잡 지표 데이터 ([View-T](https://viewt.ktdb.go.kr/cong/map/page.do))
- 환경 데이터
    - 도시별 미세먼지 데이터 ([국가통계포털](https://kosis.kr/index/index.do))
    - 도시별 오존 대기오염도 ([국가통계포털](https://kosis.kr/index/index.do))
    - CO2/NO2/SO2 대기 오염도 ([국가통계포털](https://kosis.kr/index/index.do))
    - 전국 도시 공원 정보 데이터 ([공공데이터포털](http://data.go.kr))
- 지역 경제 데이터
    - 주민등록인구 및 세대 현황 ([행정안전부](https://www.mois.go.kr/frt/a01/frtMain.do))
    - 행정구역 면적 데이터 ([국가통계포털](https://kosis.kr/index/index.do))
    - 관광 지출액 데이터 ([한국관광데이터랩](https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do))
    - 관광지 개수 및 관광객 수 데이터 ([한국관광데이터랩](https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do))