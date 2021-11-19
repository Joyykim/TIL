# 스프링 @Transactional 파보기

- @Transactional 이란?
- 구현 - 스프링 AOP, PSA
- 다양한 파라미터들
- 주의점


### 참고

- [스프링 공식문서 - 트랜잭션 관리](https://docs.spring.io/spring-framework/docs/3.0.x/spring-framework-reference/html/transaction.html) - 10.5 Declarative transaction management (선언적 트랜잭션 관리)



# @Transactional 이란?

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

# 다양한 파라미터들

String transactionManager() default "";
- ㅇ



Propagation propagation() default Propagation.REQUIRED;

Isolation isolation() default Isolation.DEFAULT;

int timeout() default TransactionDefinition.TIMEOUT_DEFAULT;

boolean readOnly() default false;



Class<? extends Throwable>[] rollbackFor() default {};

String[] rollbackForClassName() default {};



Class<? extends Throwable>[] noRollbackFor() default {};

String[] noRollbackForClassName() default {};



# 주의점

- 테스트 롤백
- 테스트 propagation
- mark rollback
- 내부에서 호출 안됨 - 프록시 이슈

