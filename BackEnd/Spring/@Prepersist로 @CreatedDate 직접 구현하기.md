## BaseTimeEntity 변경점 - `@CreatedDate` 제거, `@PrePersist` 로 변경

<img width="663" alt="스크린샷 2021-10-05 오후 6 13 55" src="https://user-images.githubusercontent.com/56679885/135995219-08be7a53-9981-4088-8f4c-da760b64209f.png">
이 전까지는 위와 같이 createdAt을 `@CreatedDate` 어노테이션과 `@EntityListeners(AuditingEntityListener.class)`로 구현되어있었다. 운영에서는 문제없이 잘 돌아갔지만 언젠가 createdAt을 내가 원하는 값으로 저장해서 테스트를 할 필요가 생겼다.

<br>

setter를 사용하긴 싫어서 createdAt을 초기화하는 생성자를 만들어주고 하위 엔티티에서 super 생성자로 createdAt을 설정해줬다. 그리고 테스트는 잘 돌아갔다.
<img width="660" alt="스크린샷 2021-10-05 오후 9 37 46" src="https://user-images.githubusercontent.com/56679885/136023813-70d20df6-8e6e-4720-bfa1-6a412663a97d.png">
<img width="673" alt="스크린샷 2021-10-05 오후 9 40 19" src="https://user-images.githubusercontent.com/56679885/136024223-aa1dc60c-8d16-45d4-b4cf-d7ae44e80e73.png">

<br>

하지만 Repository 테스트에서 위의 방법으로 createdAt를 설정하니 제대로 동작하지 않았다. 내가 원하는 값을 넣어줘도 엔티티가 persist되는 시점에 그 값을 무시하고 persist되는 현재 시간대로 새로 설정되어버렸다. 이전까지의 테스트에서는 영속상태로 만들지 않아서 잘 동작하고 있던 것이었다. persist후에 setter를 사용해 업데이트하는 것도 되지 않았다. 다시 조회해보니 persist 시점의 생성시간으로 되돌아가 있었다. 아마 `@CreatedDate`의 기능이 있는 듯 한데, 좀 더 알아봐야겠다.

결국 `@PrePersist` 어노테이션을 사용해서 현재시간으로 필드의 값을 채워주도록 했다.
`@CreatedDate`는 내부적으로 `@PrePersist` 어노테이션을 사용해서 엔티티가 영속화되기 직전에 값을 채운다. 이 때 createdAt 필드에 값이 있는지 없는지는 상관없이 새로 넣어버린다. 그래서 직접 해주기로 했고, 영속화 시점에 이미 값이 있다면 새로 설정하지 않도록 했다.

<img width="789" alt="스크린샷 2021-10-05 오후 6 24 06" src="https://user-images.githubusercontent.com/56679885/135996837-49cfd6ee-b677-410b-ab37-413b2563ff87.png">

`@PrePersist`는 `@Entity` 클래스, `@MappedSuperclass` 클래스, `@EntityListeners`에 등록한 리스너 클래스의 메서드에만 붙일 수 있다. 여기선 굳이 리스너 클래스를 만들 필요가 없어서 BaseTimeEntity에 바로 만들었다.

혹시 `@CreatedDate` 내부 동작하는 방식을 보고싶다면 `AuditingEntityListener`의 touchForCreate(), `AuditingHandlerSupport`의 touch(), touchDate()를 보면 될거야.
