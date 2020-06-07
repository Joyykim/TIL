# HTTP METHODS

출처: HTTP1.1 rfc7231 section-4 Request Methods<br>
https://tools.ietf.org/html/rfc7231#section-4

## Common Method Properties

HTTP Methods는 메소드의 성격을 나타내는 속성을 가지고 있습니다. 이 속성들을 알고 있으면 HTTP Methods의 설계 의도를 더 잘 이해할 수 있습니다. 한 메소드는 여러 속성들을 가질 수 있습니다.


### Safe Methods

어떤 메소드가 Safe Method라고 함은 이 메소드로 요청을 보낼 때 서버의 리소스에 변화를 주지 않는 "Read-only" 요청이어야 한다는 뜻입니다.

This definition of safe methods does not prevent an implementation from including behavior that is potentially harmful, that is not entirely read-only, or that causes side effects while invoking a safe method.

safe methods 정의는 설계 의도일뿐 실제 구현에서의 잠재적인 위험을 방지해주진 않습니다. 예를 들어 리소스를 생성하거나 삭제하는 요청을 GET 메소드로 작성하는 것도 가능합니다. 따라서 개발자 스스로 판단하여 상황에 적절한 HTTP메소드를 사용해야 합니다.

However, this is not mandated by the standard, and it is explicitly acknowledged that it cannot be guaranteed.

GET, HEAD, OPTIONS, TRACE 는 safe methods입니다.

### Idempotent Methods

한 번 혹은 여러 번 실행됐는지에 상관없이 같은 결과를 반환한다면(리소스에 변화가 없다면) 그 메소드는 멱등성이 있다고 말합니다.

예를 들어 파이썬에서 절댓값을 반환하는 함수인 abs()는 멱등성이 있는 함수입니다. 반환값으로 abs함수를 여러번 실행해도 한번 실행한 값과 동일하기 때문입니다.

```python
abs(-10) == abs(abs(abs(-10))) == 10
```

메소드가 멱등성이 있다는 말은 이 메소드로 같은 요청을 여러번 해도 서버의 리소스에 변화가 없어야 한다는 뜻입니다.

GET, HEAD, PUT, DELETE, TRACE, OPTIONS 메소드들은 멱등성이 있게 구현해야 합니다. PATCH는 멱등성에 대한 정확한 정의가 없는 특수한 메소드입니다. PATCH 메소드에 대해서는 뒤에서 자세히 알아보겠습니다.


### Cacheable Methods

