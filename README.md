# Docker_Project
Springboot, nginx, docker-compose 과제

### 프로젝트 목표
웹 어플리케이션을 Docker 를 통해 서비스
* Load-Balancer 1개 (Nginx Reverse proxy 80 port, Round robin 구성)
* Web Application Server 3개 (Container scale in/out 가능 - docker-compose.yml, nginx.conf 파일 수정 필요)

### 빌드 환경
* Ubuntu 16.08
* Java 1.8.0_191
* Python 2.7.12
* Docker 18.06.1
* Docker-compose 1.8.0

### 빌드 및 테스트 순서
	$ git clone https://github.com/jkinject/Docker_Project.git
	$ cd Docker_Project/webserver/sample-web-ui/
	$ ./gradlew build -x test
	$ cd ../../
	$ python devops.py start
	$ python devops.py [stop | restart | deploy]

### 스크립트 사용법
	$ python devops.py [start | stop | restart | deploy]
----
* start : 컨테이너 환경 전체 실행
* stop : 컨테이너 환경 전체 중지
* restart : 컨테이너 환경 전체 재시작
* deploy : 웹어플리케이션 무중단 배포

Web Application 수정후 위 script로 무중단 deploy 가능 (※ deploy는 start이후 진행해야함)

### Web Application 기능 추가
* 컨테이터 환경 전체 실행후 https://localhost/health 접속시 Json Type으로 IP주소를 반환
