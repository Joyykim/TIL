# HTTP METHODS

출처: HTTP1.1 rfc7231 section-4 Request Methods<br>
https://tools.ietf.org/html/rfc7231#section-4

## Common Method Properties

### Safe Methods

서버의 리소스에 변화를 주지 않는 "Read-only" 메소드.

This definition of safe methods does not prevent an implementation from including behavior that is potentially harmful, that is not entirely read-only, or that causes side effects while invoking a safe method.

safe methods 정의는 설계 의도일뿐 실제 구현에서의 잠재적인 위험을 방지해주진 않는다. 예를 들어 리소스를 생성하거나 삭제하는 요청을 GET 메소드로 작성하는 것도 가능하다. 따라서 개발자 스스로 판단하여 적절한 HTTP메소드를 사용해야 한다.



### Idempotent Methods


### Cacheable Methods