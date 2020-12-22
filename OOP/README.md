# OOP 공부

## 원리

### 왜 객체지향인가

모든 소프트웨어 모듈에는 세 가지 목적이 있다.

- 첫 번째 목적은 실행 중에 `제대로 동작`하는 것이다. 이것은 모듈의 존재 이유라고 할 수 있다.
- 두 번째 목적은 `변경을 위해 존재`하는 것이다. 대부분의 모듈은 생명주기 동안 변경되기 때문에 `간단한 작업만으로도 변경이 가능`해야 한다. 변경하기 어려운 모듈은 제대로 동작하더라도 개선해야 한다.
- 모듈의 세 번째 목적은 `코드를 읽는 사람과 의사소통`하는 것이다. 모듈은 특별한 훈련 없이도 개발자가 `쉽게 읽고 이해`할 수 있어야 한다. 읽는 사람과 의사소통할 수 없는 모듈은 개선해야 한다.

**그렇다면 모듈을 그 목적에 올바르게 만들기 위해선?**

첫번째는 너무나 당연한 이야기이니 넘어가자. 두번째, 세번째 목적을 달성하려면 훨씬 많은 고민과 노력이 필요하다.
"변경이 가능해야 한다" 하지만 어떻게? 간단한 작업만으로도! 그렇다면 변경을 어렵게 하는 요인은 무엇이 있을까?

많은 요인이 있지만 그 중 `의존성`이란 개념이 아주 중요하다.
`의존성`이란 ~(설명)
"의존성이 있다"는 곧 "변경이 될 수 있다"는 말과 같다.
So, `결합도`를 낮춘다.

How? 캡슐화를 통해 내,외부의 경계를 명확히하여 자율성을 보장하여 의존성을 줄인다.<br>
구현과 인터페이스로 나눠서 인터페이스로만 메시지를 주고받는다<br>
객체에 책임을 주어 할당하여 자율적으로 처리하도록 하자. 이로 인해 응집도를 높인다.

객체지향은 설계에 대한 방법론이다.
객체지향적 설계를 잘하려면 어떤 변경이 일어날 수 있는지 예상해야 한다?
결국 도메인을 잘 알아야 변경을 적절히 예상하여 설계할 수 있다.


### OOP 특징

- 강한 응집, 약한 결합을 지향
- 캡슐화/은닉화
- 추상화
- 다형성
- 상속

[OOP의 특징](https://gmlwjd9405.github.io/2018/07/05/oop-features.html)

### SOLID
> 객체지향 설계 5 원칙

- SRP
	- 단일 책임 원칙 (Single responsibility principle)
	- "한 클래스는 하나의 책임만 가져야 한다."

- OCP
	- 개방-폐쇄 원칙 (Open/closed principle)
	- "소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다."

- LSP
	- 리스코프 치환 원칙 (Liskov substitution principle)
	- "프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다."

- ISP
	- 인터페이스 분리 원칙 (Interface segregation principle)
	- "특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다."

- DIP
	- 의존관계 역전 원칙 (Dependency inversion principle)
	- "상위 수준의 모듈은 하위 수준의 모듈에 의존해서는 안 된다. 둘 모두 추상화에 의존해야 한다."
	- "추상화는 구체적인 사항에 의존해서는 안 된다. 구체적인 사항은 추상화에 의존해야 한다."

[객체지향 개발 5대 원칙: SOLID](http://www.nextree.co.kr/p6960/)

[SOLID 원칙](https://johngrib.github.io/wiki/SOLID/)

## 실천

### 오브젝트: 코드로 이해하는 객체지향 설계
객체지향으로 향하는 첫걸음은 클래스가 아니라 객체를 바라보는 것에서부터 시작한다. 객체지향으로 향하는 두번째 걸음은 객체를 독립적인 존재가 아니라 기능을 구현하기 위해 협력하는 공동체의 존재로 바라보는 것이다. 세번째 걸음을 내디딜 수 있는지 여부는 협력에 참여하는 객체 들에게 얼마나 적절한 역할과 책임을 부여할 수 있느냐에 달려 있다. 객체지향의 마지막 걸음은 앞에서 설명한 개념들을 여러분이 사용하는 프로그래밍 언어라는 틀에 흐트러짐 없이 담아낼 수 있는 기술을 익히는 것이다.

[책임과 메시지 그리고 캡슐화](https://it-mesung.tistory.com/106)

[오브젝트 리뷰 1](http://sculove.github.io/blog/2019/07/31/object-book1/)
[오브젝트 리뷰 2](http://sculove.github.io/blog/2019/08/10/object-book2/)
[리뷰](https://joshuabc.tistory.com/43?category=644286)

[우아한 객체지향(의존성의 관점에서 본 객체지향) - 조영호](https://www.youtube.com/watch?v=dJ5C4qRqAgA&t=956s)
[리뷰](https://github.com/jojoldu/review/tree/master/%EC%9A%B0%EC%95%84%ED%95%9C_%ED%85%8C%ED%81%AC%ED%86%A1/2019_06_20)

[객체지향 생활 체조 원칙 9가지 (from 소트웍스 앤솔러지)](https://jamie95.tistory.com/entry/Java-%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5-%EC%83%9D%ED%99%9C-%EC%B2%B4%EC%A1%B0-%EC%9B%90%EC%B9%99-9%EA%B0%80%EC%A7%80-from-%EC%86%8C%ED%8A%B8%EC%9B%8D%EC%8A%A4-%EC%95%A4%EC%86%94%EB%9F%AC%EC%A7%80)

[일급 컬렉션](https://jojoldu.tistory.com/412?category=635881)

[Enum 활용](https://woowabros.github.io/tools/2017/07/10/java-enum-uses.html)

[객체지향 연습 프로젝트 - 블랙잭](https://jojoldu.tistory.com/62?category=635881)
[블랙잭 깃헙 레포](https://github.com/jojoldu/oop-java)

[생각하라, 객체지향처럼](https://woowabros.github.io/study/2016/07/07/think_object_oriented.html)