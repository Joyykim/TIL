5/19
함수, 제너레이터, 데코레이터, 에러 처리

dictionary의 bucket에 저장 시 hash 값이 중복되었을 때 내부 구조
이진 탐색: log n
바이너리 트리에서 값이 편향되었을 때
Red black  셀프 밸런스를 맞추는 알고리즘

# 함수 Function
함수를 쓰는 이유: 코드의 재사용
정의(definition)
호출(call)

파이썬 리턴 값은 여러 개가 올 수 있다!
Tuple로 packing되서 오기 때문에 그대로 써도 되고 unpacking해도 됨


## Convention
함수 작성 시 항상 return값 주기!
테스트 코드 작성이나 디버깅 할 때 너무 힘듦…

함수 이름은 항상 동사로 작성
Ex) def do_something():

type hinting 적극적으로 사용하기
def is_odd_number(number: int) -> bool:

## 함수 정의
함수 

## 함수 호출
위치 인자:
호출 할 때 인자를

키워드 인자:
함수 정의 시 default 값을 설정한 파라미터.
키워드 인자를 위치 인자처럼 사용 가능하지만 혼선방지를 위해 지양
키워드 인자는 항상 호출 시 키워드로 하기


## Call by value, Call by reference
Value: 인자를 전달하면 letteral 값이 파라미터로 넘어간다.
Reference: 인자의 주소 값이 파라미터로 넘어간다.

## 위치인자 모으기 *, 키워드 인자 모으기 **
*args, **kwargs 는 옵션이라서 호출 시 전달하지 않아도 됨!

# Decorator
함수 정의 시 위에 @데코함수 이름을 써서 

# Error Control
오류 처리를 올바르게 하면서 Log 잘 적재해야 디버깅 가능하다.
Global 하게 except 처리 가능하지만 세부적으로 처리하는게 좋다.
raise 키워드로 예외를 발생시키는 것도 가능
else 키워드: java의 finally키워드와 같음
try 구문 안에 있는 코드는 느리다
