# GCP, Microsoft NNI를 이용한 ML-Pipeline


 > DevFest Pangyo 2019 - ML Pipeliner 프로젝트

## 과정

* 데이터를 다운받아서 Bigquery에 적재한다. 
* 데이터를 받아서 학습 실험 관리 Opensource인 Microsoft NNI를 사용해 AutoML을 수행한다. 
* 학습이 완료되면 Model Validation을 자동으로 수행해서 지금 서빙되고 있는 모델보다 우수한지 자동으로 검증한다.
* 학습된 가중치를 storage에 저장한다. 
* 모델리스트를 관리하고, 선택적으로 배포 및 롤백이 가능하게 한다. 

## 진행

1. install google cloud python API

<code>$pip install --upgrade google-cloud-storage</code>

<code>$pip install --upgrade google-cloud-bigquery</code>
#
2. Download Fashion MNIST dataset

<code>python data//make_data.py</code>

3. Upload on BigQuery

<code> gzip data/*.txt </code>

<code> bq load --source_format=CSV -F":" fashion_mnist.train data/train.txt.gz "key:integer, image:string,label:integer"</code>

<code> bq load --source_format=CSV -F":" fashion_mnist.test data/test.txt.gz "key:integer, image:string,label:integer"</code>
