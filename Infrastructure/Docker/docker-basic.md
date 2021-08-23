# 도커 기본

## 도커란?
https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html


## 도커 run 옵션
- `-it`
- `-rm` : 프로세스 중지시 컨테이너 삭제시킴
- `-e` : 컨테이너 환경변수 설정
- `--link` : 

### -name
컨테이너의 이름을 지정

### -p (포트포워딩)
컨테이너와 호스트의 포트를 연결

### -v (마운트)
컨테이너와 호스트의 디렉토리를 연결

### -d (detached 모드)
컨테이너를 백그라운드에서 실행.
-d 옵션을 사용하면 컨테이너가 detached 모드에서 실행되며, 실행 결과로 컨테이너 ID만을 출력.
<img width="722" alt="스크린샷 2021-08-23 오후 4 36 50" src="https://user-images.githubusercontent.com/56679885/130408776-7a3d3d52-6a94-48a3-9e72-e386d96cd2ee.png">
