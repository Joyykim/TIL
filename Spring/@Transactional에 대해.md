# 스프링 @Transactional 파보기

- @Transactional 이란?
- 구현 - 스프링 AOP, PSA
- 다양한 파라미터들
- 주의점


### 참고

- [스프링 공식문서 - 트랜잭션 관리](https://docs.spring.io/spring-framework/docs/3.0.x/spring-framework-reference/html/transaction.html) - 10.5 Declarative transaction management (선언적 트랜잭션 관리)



# `@Transactional` 이란?

`선언적 트랜잭션`이라고 한다. 트랜잭션 처리를 코드상에서 직접 하지 않아도 되고, 어노테이션을 붙이는 것만으로 쉽게 사용할 수 있다. (`선언형 프로그래밍` 참고)

메서드, 클래스, 인터페이스 붙여서 사용할 수 있다. 

> 스프링은 `@Transactional`을 인터페이스가 아닌 구현 클래스에 붙이기를 권장하고 있다. 
>
> 인터페이스 (또는 인터페이스 메소드)에 @Transactional 어노테이션을 배치 할 수 있지만 이는 인터페이스 기반 프록시를 사용하는 경우 예상 한 대로만 작동합니다. Java 주석이 인터페이스에서 상속되지 않는다는 사실은 클래스 기반 프록시 (proxy-target-class = “true”) 또는 위빙 기반 측면 (mode = “aspectj”)을 사용하는 경우 트랜잭션 설정이 다음과 같음을 의미합니다. 프록시 및 위빙 인프라에 의해 인식되지 않으며 객체가 트랜잭션 프록시에 래핑되지 않으므로 확실히 나쁠 것입니다.
>
> Tip
> Spring recommends that you only annotate concrete classes (and methods of concrete classes) with the `@Transactional` annotation, as opposed to annotating interfaces. You certainly can place the `@Transactional` annotation on an interface (or an interface method), but this works only as you would expect it to if you are using interface-based proxies. The fact that Java annotations are *not inherited from interfaces* means that if you are using class-based proxies (`proxy-target-class="true"`) or the weaving-based aspect (`mode="aspectj"`), then the transaction settings are not recognized by the proxying and weaving infrastructure, and the object will not be wrapped in a transactional proxy, which would be decidedly *bad*.
>
> [스프링 공식문서 - 트랜잭션 관리](https://docs.spring.io/spring-framework/docs/3.0.x/spring-framework-reference/html/transaction.html) ("10.5.6 Using @Transactional" 파트의 Tip)

- 메서드가 시작할 때 transaction `begin`, 종료된 후 `commit`을 자동 수행해준다.
- 예외가 발생하면 `rollback` 처리를 자동 수행해준다.

# `@Transactional`의 AOP 프록시 매커니즘

스프링에서 `@Transactional`의 AOP로 구현한다.
스프링의 프록시 매커니즘에는 두 가지 - JDK Dynamic Proxy, CGLIB Proxy 가 있다.
스프링부트에서는 CGLIB Proxy가 default로 사용된다.

### JDK Dynamic Proxy

- 인터페이스에 대한 Proxy만을 지원, 클래스에 대한 Proxy를 지원할 수 없다.
- Target 클래스에 Proxy를 적용할 때 PointCut을 통해 Advice되는 메서드를 지정한다. JDK Proxy를 사용하면 **Target 클래스에 대한 모든 메서드 호출(PointCut으로 지정하지 않은 메서드도)이 일단 JVM에 Intercept된다**(이 때 reflection이 사용된다). 그 후에 메서드의 Advice 적용 여부를 판단하게 된다.
  - 이는 JDK Dynamic Proxy의 실행속도를 저하시키는 원인이 된다.

### CGLIB Proxy

- CGLIB Proxy는 클래스에 대한 Proxy가 가능하다.
- CGLIB Proxy도 JDK Proxy처럼 Runtime시에 Target 메서드가 호출될 때 해당 메서드의 Advice 적용 여부를 결정하게 된다. 그러나 CGLIB는 **메서드가 처음 호출 되었을때 동적으로 bytecode를 생성하고 이후 호출에서는 재사용**하여 두번째 호출 이후부터는 실행속도가 향상된다.

### Spring Boot에서 기본으로 CGLIB를 선택한 이유

예전에는 CGLIB에 3가지의 한계점이 있었고, 때문에 권장되지 않았다.
1. net.sf.cglib.proxy.Enhancer 의존성 추가
2. 타깃 클래스에 파라미터가 없는 디폴트 생성자 필요
3. 생성된 Proxy의 메소드를 호출하게 되면 타깃의 생성자가 두 번 호출됨.

하지만 Spring boot 1.4(Spring 4.3) 부터는 `@Transactional`은 기본적으로 CGLIB Proxy로 동작한다. [Spring boot 1.4 release note](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-1.4-Release-Notes#transactional-default-to-cglib-proxies)

1. Spring Core 패키지에 포함됨 - `net.sf.cglib.proxy.Enhancer` -> `org.springframework.cglib.proxy`
2. objenesis 라이브러리를 사용
  1. 디폴트 생성자가 필요없어짐
  2. 생성자가 두 번 호출되던 문제 해결

기존에 CGLIB가 가지고 있던 한계점들이 개선되었기 때문에 JDK Dynamic Proxy보다 성능이 좋은 CGLIB Proxy를 `@Transactional`의 기본 프록시 매커니즘으로 선택하게 된 것이다.

출처
- https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-1.4-Release-Notes#transactional-default-to-cglib-proxies
- https://gmoon92.github.io/spring/aop/2019/04/20/jdk-dynamic-proxy-and-cglib.html
- http://blog.breakingthat.com/2018/04/03/springboot-transaction-%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98/

# `@Transactional`의 속성들(파라미터)

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
커넥션을 readOnly로 만들고 CUD sql을 실행하려 하면 에러가 터질 수 있는데, JDBC 벤더사 마다 동작방식이 조금씩 다르다.

- MySQL Driver는 5.6.5 이상부터 지원
- Oracle Driver는 예전부터 readOnly 옵션을 제공
- H2에서는 아직 지원을 하지 않음

출처
- https://tech.yangs.kr/22
- http://wonwoo.ml/index.php/post/839

### readOnly=true 설정시 성능향상

**1. JPA, 하이버네이트**

엔티티가 영속성 컨텍스트에 관리되면 1차 캐시부터 변경 감지까지 얻을 수 있는 혜택이 많다.
하지만 영속성 컨텍스트는 변경 감지를 위해서 스냅샷 인스턴스를 보관하므로 더 많은 메모리를 사용하는 단점이 존재한다.

- flush 호출하지 않음
- dirty checking(변경 감지)하지 않음

readOnly=true 옵션을 주면 스프링 프레임워크가 하이버네이트 세션 플러시 모드를 MANUAL로 설정한다.
이렇게 하면 강제로 플러시를 호출하지 않는 한 플러시가 일어나지 않는다.
따라서 트랜잭션을 커밋하더라도 영속성 컨텍스트가 플러시 되지 않아서 엔티티의 등록, 수정, 삭제가 동작하지 않는다.

flush 할 때 일어나는 스냅샷 비교와 같은 무거운 로직을 수행하지 않으므로 성능이 향상된다.

출처
- https://cheese10yun.github.io/jpa-flush/

<br>

**1-1.스프링 5.1 이후 사용시 - 읽기 전용 쿼리 힌트 자동적용**

`@Transaction(readOnly=true)`로 설정 시, 하이버네이트 전용 힌트인 `org.hibernate.readOnly`(읽기 전용 쿼리 힌트)가 자동으로 true로 동작한다.
`org.hibernate.readOnly`를 사용하면 **영속성 컨텍스트가 스냅샷을 저장하지 않아서** 메모리 사용량을 최적화 할 수 있다.
스냅샷만 저장하지 않는 것이지, 1차 캐시에는 그대로 저장한다. 똑같은 식별자로 2번 조회했을 경우 반환되는 엔티티의 주소가 같다.

출처
- https://www.inflearn.com/questions/31497
- https://joont92.github.io/jpa/JPA-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94/

<br>

**2. MySQL - InnoDB Read-Only Transactions**

readOnly 트랜잭션은 transaction ID(TRX_ID field)를 세팅하는 오버헤드를 줄일 수 있다.
transaction ID는 쓰기 작업이나 `SELECT ... FOR UPDATE` 같은 lock을 거는 읽기 작업에서 필요한데, readOnly 트랜잭션에선 필요하지 않다.

> InnoDB can avoid the overhead associated with setting up the transaction ID (TRX_ID field) for transactions that are known to be read-only. A transaction ID is only needed for a transaction that might perform write operations or locking reads such as SELECT ... FOR UPDATE. Eliminating unnecessary transaction IDs reduces the size of internal data structures that are consulted each time a query or data change statement constructs a read view.

출처
- https://dev.mysql.com/doc/refman/5.7/en/innodb-performance-ro-txn.html


## rollbackFor
`Class<? extends Throwable>[] rollbackFor() default {};`



## rollbackForClassName
`String[] rollbackForClassName() default {};`


## noRollbackFor
`Class<? extends Throwable>[] noRollbackFor() default {};`


## noRollbackForClassName
`String[] noRollbackForClassName() default {};`




# 주의점

- 테스트 롤백
- 테스트 propagation
- mark rollback
- 자신의 메서드를 호출하면 어노테이션이 붙어도 작동 안됨 - 프록시 이슈

