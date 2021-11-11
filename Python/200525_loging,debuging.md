5/25

패키지 설치, 로깅, 디버깅

# 패키지 설치

pip로만 설치를 하면 의존성 충돌이 일어날 가능성이 있습니다.

의존성 충돌이란 - 한 패키지를 설치하면 내부적으로 여러 라이브러리가 같이 설치 되는데 둘 이상의 패키지에서 하나의 라이브러리를 요구할 때 요구하는 라이브러리 버전이 다르면 충돌이 일어납니다.

이러한 이슈때문에 현업에서는 pip는 거의 쓰지 않습니다.

pip freeze > requirements.txt: 지금 설치된 패키지 목록 파일로 저장
pip install -r requirements.txt: 파일 목록에서 패키지 설치

장고 패키지 목록 사이트
awesome django: https://github.com/wsvincent/awesome-django


# 로깅

에러 발생 시 대처할 수 있는 유일한 방법!
로깅만 잘해도 칭찬받는당

로깅 레벨

1. debug
2. info: 실서버 로깅 시작 레벨
3. warning: 실서버 로깅 시작 레벨
4. error
5. critical

## Application Log
개발자 디버깅용 로그<br>
TMI 수준으로 상세하게 남겨야 디버깅에 용이하다<br>
고유하고 변경 불가능한 데이터를 중점적으로 로깅<br>
적당한 retention 필요. 즉 보관을 얼마나 오래 할지도 고려해야함 - 서버 하드용량 문제?

육하원칙으로 상세하게…

## User Log
통계/분석용 사용자 패턴 로그<br>
retention이 매우 길고 보통 영구 저장을 함 - 데이터 엔지니어 영역<br>
누락 되거나 잘못 저장되면 매출 계산에 큰 영향을 끼치므로 매우 안전해야 함

DevOps - SE 시스템 엔지니어 - 인프라 관리

요즘은 파일로그보단 외부로 로깅 서버를 따로 빼서 관리.

# 디버깅
파이참 디버깅: https://youtu.be/ST4WEosRiY4
break point를 지정하고 프로그램 실생하면 break에 프로그램이 멈추고 변수 확인 및 코드 실행 동적으로 가능