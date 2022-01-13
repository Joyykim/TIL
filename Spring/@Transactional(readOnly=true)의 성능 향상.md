## 1. JPA, 하이버네이트

엔티티가 영속성 컨텍스트에 관리되면 1차 캐시부터 변경 감지까지 얻을 수 있는 혜택이 많다.  
하지만 영속성 컨텍스트는 변경 감지를 위해서 스냅샷 인스턴스를 보관하므로 더 많은 메모리를 사용하는 단점이 존재한다.

- flush 호출하지 않음
- dirty checking(변경 감지)하지 않음

readOnly=true 옵션을 주면 스프링 프레임워크가 하이버네이트 세션 플러시 모드를 MANUAL로 설정한다.  
이렇게 하면 강제로 플러시를 호출하지 않는 한 플러시가 일어나지 않는다.  
따라서 트랜잭션을 커밋하더라도 영속성 컨텍스트가 플러시 되지 않아서 엔티티의 등록, 수정, 삭제가 동작하지 않는다.

flush 할 때 일어나는 스냅샷 비교와 같은 무거운 로직을 수행하지 않으므로 성능이 향상된다.

참고

- [https://cheese10yun.github.io/jpa-flush/](https://cheese10yun.github.io/jpa-flush/)

### 1-1. 스프링 5.1 이후 사용시 - 읽기 전용 쿼리 힌트 자동적용

`@Transaction(readOnly=true)`로 설정 시, 하이버네이트 전용 힌트인 `org.hibernate.readOnly`(읽기 전용 쿼리 힌트)가 자동으로 true로 동작한다.  
`org.hibernate.readOnly`를 사용하면 **영속성 컨텍스트가 스냅샷을 저장하지 않아서** 메모리 사용량을 최적화 할 수 있다.  
스냅샷만 저장하지 않는 것이지, 1차 캐시에는 그대로 저장한다. 똑같은 식별자로 2번 조회했을 경우 반환되는 엔티티의 주소가 같다.

참고

- [https://www.inflearn.com/questions/31497](https://www.inflearn.com/questions/31497)
- [https://joont92.github.io/jpa/JPA-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94/](https://joont92.github.io/jpa/JPA-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94/)

## 2. MySQL - InnoDB Read-Only Transactions

readOnly 트랜잭션은 transaction ID(TRX\_ID field)를 세팅하는 오버헤드를 줄일 수 있다.  
transaction ID는 쓰기 작업이나 `SELECT ... FOR UPDATE` 같은 lock을 거는 읽기 작업에서 필요한데, readOnly 트랜잭션에선 필요하지 않다.

> InnoDB can avoid the overhead associated with setting up the transaction ID (TRX\_ID field) for transactions that are known to be read-only. A transaction ID is only needed for a transaction that might perform write operations or locking reads such as SELECT ... FOR UPDATE. Eliminating unnecessary transaction IDs reduces the size of internal data structures that are consulted each time a query or data change statement constructs a read view.

참고

- [https://dev.mysql.com/doc/refman/5.7/en/innodb-performance-ro-txn.html](https://dev.mysql.com/doc/refman/5.7/en/innodb-performance-ro-txn.html)
