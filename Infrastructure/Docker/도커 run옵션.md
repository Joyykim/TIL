# 도커 run 옵션
https://www.daleseo.com/docker-run/

### --name
컨테이너의 이름을 지정.
name을 지정하지 않고 실행한다면 도커가 임의로 이름을 만들지만 우리가 이해하기 쉬운 이름을 꼭 붙여주자.
도커 네트워크의 bridge모드에선 컨테이너를 링크시킬 때 name을 참조한다.

### -d (Detached 모드)
컨테이너를 백그라운드(Detached 모드)에서 실행. 도커 실행은 Foreground/Detached 모드가 있는데 Foreground가 디폴트다. Foreground 모드에도 여러 옵션들이 있지만 대부분 백그라운드에서 실행하니 패스.
-d 옵션을 붙이지 않고 실행한다면, `^C`로 프로세스 중지시 컨테이너가 중지된다.
