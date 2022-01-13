# `@Transactional`의 AOP 프록시 매커니즘

스프링에서 `@Transactional`은 AOP로 구현한다.
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

참고
- https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-1.4-Release-Notes#transactional-default-to-cglib-proxies
- https://gmoon92.github.io/spring/aop/2019/04/20/jdk-dynamic-proxy-and-cglib.html
- http://blog.breakingthat.com/2018/04/03/springboot-transaction-%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98/
