# Serializers

직렬화란
오브젝트를 "직렬화한다"는 것은 오브젝트의 상태를 오브젝트의 사본으로 다시 변환할 수 있는 바이트 스트림으로 변환하는 것을 의미한다.
https://ko.wikipedia.org/wiki/%EC%A7%81%EB%A0%AC%ED%99%94

marshalling == 직렬화(Serialize): 파이썬에서만
https://ko.wikipedia.org/wiki/%EB%A7%88%EC%83%AC%EB%A7%81_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99)


### docstrings

Serializers and ModelSerializers are similar to Forms and ModelForms.
Unlike forms, they are not constrained to dealing with HTML output, and
form encoded input.

Serialization in REST framework is a two-phase process:

1. Serializers marshal between complex types like model instances, and
python primitives.
2. The process of marshalling between python primitives and request and
response content is handled by parsers and renderers.

