# Cloud Dataflow 파이프라인의 예측 머신러닝 모델

<img src="https://cloud.google.com/dataflow/images/faster-development-easier-management.png">

ML 모델을 Cloud Dataflow 파이프라인에 통합하는 작업에는 다양한 접근 방식이 있으며 그중 시스템 요구사항에 가장 적합한 접근 방식을 선택해야 한다.

시스템 요구사항으로 다음을 고려해야한다:
1. 처리량
2. 지연 시간
3. 비용
4. 구현
5. 유지보수

이러한 고려사항의 균형을 맞추는 것은 항상 간단하지만은 않지만 이 프로젝트 결과를 사용하면 우선순위에 따라 의사 결정 프로세스를 처리하는 데 도움이 된다. 프로젝트는 일괄 및 스트림 데이터 파이프라인에서 TensorFlow를 통해 학습하는 머신러닝(ML) 모델을 사용하여 예측을 수행하는 세 가지 접근 방식을 비교한다.

1. 배포된 모델을 파이프라인 스트리밍용 REST/HTTP API로 사용
2. 일괄 파이프라인에 AI Platform(AI Platform) 일괄 예측 작업 사용
3. 일괄 및 스트리밍 파이프라인에 Cloud Dataflow 직접 모델 예측 사용

모든 실험은 다양한 입력을 기반으로 아기의 체중을 예측하는 모델을 사용했으며 모델은 Natality 데이터세트로 학습하였다.

데이터 파이프라인을 실행하고 학습된 ML 모델을 호출하는 방법은 다양하지만 기능 요구사항은 항상 동일하다.

1. 제한된(일괄) 소스 또는 제한되지 않은(스트리밍) 소스에서 데이터를 수집한다. 데이터를 수집하는 소스에는 센서 데이터, 웹사이트 상호작용, 금융 거래 등이 있을 수 있다.
2. 예측에 ML 모델을 호출하여 입력 데이터를 변환 및 보강한다. JSON 파일을 파싱하여 유지관리 날짜 예측, 제품 추천 또는 사기 행위 감지를 수행하기 위해 관련 필드를 추출하는 작업을 예로 들 수 있다.
3. 분석 또는 백업을 위해 변환된 데이터와 예측을 저장하거나 Queue 시스템으로 전달하여 새 이벤트 또는 추가 파이프라인을 트리거합니다. 잠재적인 사기 행위를 실시간으로 감지하거나 대시보드에서 액세스할 수 있는 저장소에 유지관리 일정 정보를 저장하는 작업을 예로 들 수 있다.

- 배치 수준의 ETL(Extract, Transform, Load) 과정의 예측을 통해 데이터를 변환하고 보강할 경우 처리량을 극대화하여 전체 데이터 배치를 처리하는 데 필요한 전반적인 시간을 줄이는 것을 목표로 해야한다.
- 그러나, 스트리밍 데이터를 처리하여 온라인 예측을 수행할 경우 지연 시간을 최소화하여 각 예측을 실시간에 가깝게 수신하는 것을 목표로 해야한다.

이 프로젝트에서는 세 가지 주요 기술을 사용합니다.

1. Cloud Dataflow에서 실행되어 데이터를 처리하는 Apache Beam
2. ML 모델을 구현하고 학습하는 TensorFlow
3. 일부 실험에서 AI Platform을 ML 모델의 호스팅 플랫폼으로 사용하여 일괄 및 온라인 예측을 수행하였다.

[ 소개 ] 
- Apache Beam은 스트리밍 및 일괄 데이터 처리 작업을 모두 실행하는 오픈소스 통합 프로그래밍 모델이다.
- Cloud Dataflow는 서버 없이도 Apache Beam 작업을 실행할 수 있는 GCP 제품이다.
- AI Platform은 DevOps에 필요한 관리를 최소화하여 대규모로 TensorFlow 모델을 학습, 초매개변수 조정 등의 서비스를 제공할 수 있는 serverless platform이다. platform은 온라인 예측용으로 학습된 모델을 REST API로 배포하고 일괄 예측 작업을 할 수 있도록 지원한다. 

[ 일괄 처리 아키텍처 ]
<img src="https://cloud.google.com/solutions/images/comparing-ml-model-predictions-using-cloud-dataflow-fig-1-batch-processing.svg">

[ 스트림 처리 아키텍처 ]
<img src="https://cloud.google.com/solutions/images/comparing-ml-model-predictions-using-cloud-dataflow-fig-2-stream-processing.svg">

# TensorFlow 모델 호출
TensorFlow로 학습한 모델을 호출하는 방법은 세 가지이다.
1. 온라인 예측용 HTTP 엔드포인트를 통해 호출하는 방법<br>TensorFlow 모델은 HTTP 엔드포인트로 배포되어 스트림 데이터 처리 파이프라인 또는 클라이언트 앱을 통해 실시간으로 호출되고 예측을 제공
  
2. 일괄 및 온라인 예측을 위해 저장된 모델 파일을 사용하여 직접 호출하는 방법

3. 일괄 예측을 위한 AI Platform 일괄 예측 작업을 통해 호출

AI Platform Prediction을 사용하여 HTTP 엔드포인트로 모델을 배포하려면 다음 단계를 따라야 한다.

1. 학습된 모델 파일을 Cloud Storage에서 사용할 수 있는지 확인한다.
2. <code>gcloud ml-engine models create</code> 명령어를 사용하여 모델을 만든다.
3. <code>gcloud ml-engine versions create</code>명령어를 사용하여 모델 버전을 Cloud Storage의 모델 파일과 함께 배포한다.


