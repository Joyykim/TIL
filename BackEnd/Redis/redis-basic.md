# 레디스 기초

## 레디스란
레디스는 인메모리 기반의 키-밸류 구조의 데이터베이스다.
전통적인 RDBMS와는 매우 다른 성격을 가지고 있다.
- 메모리 기반. 레디스 프로세스가 종료되면 데이터도 날라간다.
- 메인 스레드는 싱글 스레드로 운용된다.
- 데이터의 Expire(파기시간)을 설정할 수 있다.
- 캐시를 구현하는데 주로 사용된다.

## 싱글 스레드
메인 스레드는 싱글 스레드로 운용된다.
- 장점 : atomic 보장, race condition 회피
- 단점 : 오래걸리는 명령을 실행하면 다른 명령에 영향을 줌
- O(N) 명령어는 사용 자제 : KEYS, FLUSHALL, FLUSHDB, DEL 등
- 버전 6.x부터는 아래와 같은 부분에만 멀티스레드가 도입되었다.
  - 클라이언트에서 전송한 명령을 읽고 파싱하는 부분
  - 명령어 처리 결과를 클라이언트에게 전송하는 부분
  - (주의) 명령어 실행 자체는 위의 메인스레드에서 수행하므로 여전히 싱글스레드라고 봐야함

## Collection
레디스는 비슷하게 캐시목적으로 설계된 Memcached와 자주 비교되는데 Memcached와의 큰 차이점 중 하나가 Collection 지원 여부이다.
Collection을 통해 훨씬 편리하고 구조적으로 데이터를 관리할 수 있다.
레디스는 (String, Bitmap, Hash, List, Set, Sorted Set, Geospatial Index, Hyperloglog, Stream)의 컬렉션을 지원하는데 그 중 자주 쓰이는 몇 개만 알아보자.

- Strings : Vinary-safe한 기본적인 key-value 구조
- Lists : String element의 모음, 순서는 삽입된 순서를 유지하며 기본적인 자료구로 Linked List를 사용
- Sets : 유일한 값들의 모임인 자료구조, 순서는 유지되지 않음
- Sorted sets : Sets 자료구조에 score라는 값을 추가로 두어 해당 값을 기준으로 순서를 유지
- Hahses : 내부에 key-value 구조를 하나더 가지는 Reids 자료구조

## Expire
- 메모리는 한정적이니 대부분 key 에 Expire 를 설정할 것을 권장
- 동일한 key 가 다시 들어오면 timeout 이 재설정됨
- Expire는 main key 단위로만 적용할 수 있다. 개별 Collection 의 item key 단위(ex. hash key의 field 들)로는 설정할 수 없다.

### Expire 되는 타이밍
- key 에 대한 접근이 발생할 때
- (내부 스케줄러) activeExpireCycle 에 의한 삭제
- command 처리 전에 memory가 부족할 때 메모리 정책에 따라서 삭제

