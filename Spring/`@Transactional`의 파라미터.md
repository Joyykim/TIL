# `@Transactional`의 파라미터

## transactionManager
`String transactionManager() default "";`

## propagation
`Propagation propagation() default Propagation.REQUIRED;`

- `REQUIRED` (default) : 이미 시작된 트랜잭션이 있으면 참여하고 없으면 새로 시작한다. 
- `REQUIRES_NEW` : 항상 새로운 트랜잭션을 시작한다. 이미 진행 중인 트랜잭션이 있으면 트랜잭션을 잠시 보류시킨다.
- `SUPPORTS` : 이미 시작된 트랜잭션이 있으면 참여하고, 없으면 트랜잭션없이 진행한다.
- `NESTED` : 중첩된 트랜잭션은 먼저 시작된 부모 트랜잭션의 커밋과 롤백에는 영향을 받지만 자신의 커밋과 롤백은 부모 트랜잭션에게 영향을 주지 않는다. 메인 트랜잭션이 롤백되면 중첩된 로그 트랜잭션도 같이 롤백되지만, 반대로 중첩된 로그 트랜잭션이 롤백돼도 메인 작업에 이상이 없다면 메인 트랜잭션은 정상적으로 커밋된다.
- `MANDATORY` : REQUIRED와 비슷하게 이미 시작된 트랜잭션이 있으면 참여한다. 반면에 트랜잭션이 시작된 것이 없으면 새로 시작하는 대신 예외를 발생시킨다. 혼자서는 독립적으로 트랜잭션을 진행하면 안 되는 경우에 사용한다.
- `NOT_SUPPORTED` : 트랜잭션을 사용하지 않게 한다. 이미 진행 중인 트랜잭션이 있으면 보류시킨다.
- `NEVER` : 트랜잭션을 사용하지 않도록 강제한다. 이미 진행 중인 트랜잭션도 존재하면 안된다 있다면 예외를 발생시킨다.

주로 쓰이는 옵션: REQUIRED, REQUIRES_NEW, NESTED, SUPPORTS

출처
- https://oingdaddy.tistory.com/28

## isolation
`Isolation isolation() default Isolation.DEFAULT;`

## timeout
`int timeout() default TransactionDefinition.TIMEOUT_DEFAULT;`

## readOnly
`boolean readOnly() default false;`

- 해당 트랜잭션이 읽기 전용임을 DB에 알림 - 'Connection.setReadOnly(true)'
- DB Replication 설정 시 해당 트랜잭션이 slave DB에서 조회하도록 함

### DB에 읽기 전용임을 알림
'Connection.setReadOnly(true)'를 호출.
readOnly 커넥션에서 insert,update,delete sql을 실행하려 하면 에러가 터질 수 있는데, JDBC 드라이버 벤더사 마다 동작방식이 조금씩 다르다.

- MySQL Driver는 5.6.5 이상부터 지원
- Oracle Driver는 예전부터 readOnly 옵션을 제공
- H2에서는 아직 지원을 하지 않음

[`@Transactional(readOnly=true)` 설정시 성능 향상](https://github.com/Joyykim/TIL/blob/master/Spring/@Transactional(readOnly=true)%EC%9D%98%20%EC%84%B1%EB%8A%A5%20%ED%96%A5%EC%83%81.md)

참고
- https://tech.yangs.kr/22
- http://wonwoo.ml/index.php/post/839

## rollbackFor
`Class<? extends Throwable>[] rollbackFor() default {};`

`@Transactional`(줄여서 `@Tx`) 는 메서드 내에서 UncheckedException 혹은 Error가 발생하면 트랜잭션을 롤백한다. CheckedException은 롤백하지 않는다.
만약 CheckedException이 발생했을 때도 롤백하고 싶다면 

## rollbackForClassName
`String[] rollbackForClassName() default {};`



## noRollbackFor
`Class<? extends Throwable>[] noRollbackFor() default {};`


## noRollbackForClassName
`String[] noRollbackForClassName() default {};`

