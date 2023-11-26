https://docs.aws.amazon.com/ko_kr/resource-explorer/latest/userguide/getting-started-terms-and-concepts.html

# AWS Resource Explorer

리소스 검색 및 검색 서비스 입니다.
리소스 탐색기를 사용하면 인터넷 검색 엔진과 유사한 환경을 사용하여 Amazon Elastic Compute Cloud 인스턴스, Amazon Kinesis 스트림 또는 Amazon DynamoDB 테이블과 같은 리소스를 탐색할 수 있습니다. 이름, 태그, ID와 같은 리소스 메타데이터를 사용하여 리소스를 검색할 수 있습니다. 리소스 탐색기는 계정 전체에서 AWS 리전 작동하여 지역 간 워크로드를 간소화합니다.

Resource Explorer는 AWS 리소스 탐색기 서비스에서 만들고 유지 관리하는 인덱스를 사용하여 검색 쿼리에 빠르게 응답합니다. 리소스 탐색기는 다양한 데이터 소스를 사용하여 리소스에 대한 정보를AWS 계정 수집합니다. 리소스 탐색기는 리소스 탐색기가 검색할 수 있도록 해당 정보를 인덱스에 저장합니다.

## View
뷰는 인덱스에 나열된 리소스를 쿼리하는 데 사용되는 메커니즘 입니다.
인덱스에서 검색 및 검색 목적으로 표시되고 사용 가능한 정보를 정의합니다.
검색 결과에 포함되는 리소스를 제한하는 필터를 지정할 수 있습니다.

## Index
인덱스는 리소스 탐색기에서 관리되는 리소스 내의 모든 AWS 리소스에 대한 정보 모음입니다.
사용자는 인덱스를 직접 쿼리할 수 없고, 항상 뷰를 사용하여 쿼리해야 합니다.

### Local index
Resource Explorer를 활성화하는 모든 AWS 리전에 하나의 로컬 인덱스가 있습니다.
로컬 인덱스에는 동일한 리전의 리소스에 대한 정보만 포함됩니다.

### Aggregator index
Resource Explorer 관리자는 한 AWS 리전의 인덱스를 AWS 계정의 집계자 인덱스로 지정할 수도 있습니다.
집계자 인덱스는 계정에서 Resource Explorer가 켜져 있는 다른 모든 지역에 대한 인덱스 복사본을 수신하고 저장합니다.
집계자 인덱스는 자체 리전의 리소스에 대한 정보도 수신하고 저장합니다.
