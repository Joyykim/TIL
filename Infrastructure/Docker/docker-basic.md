# 도커 기본

## 도커란?
https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html


## 도커 run 옵션
- `-it`
- `-rm` : 프로세스 중지시 컨테이너 삭제시킴
- `-e` : 컨테이너 환경변수 설정
- `--link` : 

### --name
컨테이너의 이름을 지정
도커 오퍼레이터는 세가지 방법으로 컨테이너를 구분할 수 있다.
<img width="792" alt="스크린샷 2021-08-23 오후 4 53 12" src="https://user-images.githubusercontent.com/56679885/130410920-d13dc8b1-1b1a-4339-9632-950c439201da.png">

name을 지정하지 않고 실행한다면 도커가 임의로 이름을 붙여준다. 
<img width="272" alt="스크린샷 2021-08-23 오후 4 54 44" src="https://user-images.githubusercontent.com/56679885/130411117-2bd2c7e9-a996-450e-a833-cc4189984fbb.png">
이해하기 쉬운 이름을 꼭 붙여주자.

### -p (포트포워딩)
컨테이너와 호스트의 포트를 연결

### -v (마운트)
컨테이너와 호스트의 디렉토리를 연결

### -d (Detached 모드)
컨테이너를 백그라운드(Detached 모드)에서 실행. 도커 실행은 Foreground/Detached 모드가 있는데 Foreground가 디폴트다. Foreground 모드에도 여러 옵션들이 있지만 대부분 백그라운드에서 실행하니 패스.
-d 옵션을 붙이지 않고 실행한다면, `^C`로 프로세스 중지시 컨테이너가 중지된다.
