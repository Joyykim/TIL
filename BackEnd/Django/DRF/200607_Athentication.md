### Authentication
단어의 뜻 그대로 사용자를 "인증"하는 작업이다. 존재하는(그리고 유효한) 회원인지 확인한다. 유저의 아이디/비밀번호으로 인증하거나, 유저의 고유한 토큰값을 사용하거나, 클라이언트가 웹 브라우저라면 session이나 cookie(쓰다보니 session과 cookie에 대한 이해가 부족하다는것이 절실히...)를 활용해서 인증할 수 있다. 즉, 클라이언트에서는 유저를 인증할 수 있는 각종 정보를 전송하고, 서버는 이를 가지고 유저의 존재성을 확인한다.

### Authorization
Authorization 과정을 거쳐 인증된 유저에게 고유한 권한을 부여하는 것이다. 유저는 자신에게 부여된 권한에 맞는 행동만 할 수 있다. 페이스북으로 예를 들어보자. 어떤 유저 A가 있는데, 이 유저는 자신의 타임라인은 친구에게만 공개하도록 설정했다고 하자. 이 설정과정 자체가 Authorization의 실현이다. 유저 A 입장에서는 다른 유저들이 3가지로 분류된다. Anonymous(인증하지 못한), 일반 유저(친구는 아닌), 친구 유저가 그 분류다. Anonymous는 유저 A에 대해 아무 정보도 얻을 수 없고, 일반 유저는 타임라인을 제외한 프로필 사진등의 프로필 정보를 볼 수 있고, 친구 유저는 유저 A가 페이스북에 남긴 모든 정보를 볼 수 있는 것이다.

DRF를 활용하면 authentication과 authorization 과정을 API별로 손쉽게 설정할 수 있다. API 전체에 대한 설정이라면 settings.py의 "REST_FRAMEWORK" dictionary에 기술할 수 있고, 오브젝트 레벨로 세세하게 설정하고 싶다면, 그 오브젝트를 다루는 view 혹은 viewset의 "authentication_classes", "permission_classes" property에 원하는대로 기술하면 된다. 웬만한 옵션들은 또한 DRF가 제공해주니 중요한건 Authentication과 Authorization이 명확히 분리되어있으며, 분명한 선후관계를 지닌다는 것이다.