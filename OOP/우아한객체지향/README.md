### 클래스 의존성의 종류
- 연관 관계
- 의존 관계
- 상속 관계
- 실체화 관계

의존성이 필요없다면 제거

양방향 의존성 피하기 - 하나의 객체로 묶여야할 기능이 잘못 분리되어 있는건 아닌지 의심해봐야함

패키지 사이의 의존성 사이클 제거

### 의존성 관점에서의 설계

연관 관계를 구현하는 방법 중 하나는 객체 참조

객체에 메세지를 보낸다는 건 그 객체에 public 메소드로 구현된다는 뜻.
메세지를 보내야 하기 때문에 메소드를 구현한다. 메세지를 결정하고 메소드로 구현하는 것이 옳은 설계.