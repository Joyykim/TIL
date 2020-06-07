# Serializers

직렬화란
오브젝트를 "직렬화한다"는 것은 오브젝트의 상태를 오브젝트의 사본으로 다시 변환할 수 있는 바이트 스트림으로 변환하는 것을 의미한다.
https://ko.wikipedia.org/wiki/%EC%A7%81%EB%A0%AC%ED%99%94

marshalling == 직렬화(Serialize): 파이썬에서만
https://ko.wikipedia.org/wiki/%EB%A7%88%EC%83%AC%EB%A7%81_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99)

#### serializers 패키지 docstrings

Serializers, ModelSerializers는 Forms, ModelForms와 매우 유사합니다.
Unlike forms, they are not constrained to dealing with HTML output, and form encoded input.

Serialization in REST framework is a two-phase process:

1. Serializers marshal between complex types like model instances, and
python primitives.
2. The process of marshalling between python primitives and request and
response content is handled by parsers and renderers.


### BaseSerializer
모든 serializer의 가장 기본이 되는 클래스

#### BaseSerializer 클래스 docstrings

The BaseSerializer class provides a minimal class which may be used
for writing custom serializer implementations.

Note that we strongly restrict the ordering of operations/properties
that may be used on the serializer in order to enforce correct usage.

In particular, if a `data=` argument is passed then:

.is_valid() - Available.
.initial_data - Available.
.validated_data - Only available after calling `is_valid()`
.errors - Only available after calling `is_valid()`
.data - Only available after calling `is_valid()`

If a `data=` argument is not passed then:

.is_valid() - Not available.
.initial_data - Not available.
.validated_data - Not available.
.errors - Not available.
.data - Available.

If we want to be able to return complete object instances based on the validated data we need to implement one or both of the .create() and .update() methods.

### ModelSerializers

Django에서 Form 클래스와 ModelForm 클래스를 제공하듯, REST 프레임워크에서도 Serializer 클래스와 ModelSerializer 클래스를 제공합니다.
Serializers를 사용하면 Model에서의 필드 명시와 Serializers 필드 명시가 중복되죠? 
이런 코드는 유지보수하기 어렵고 일관성이 없습니다. 
ModelSerializers에선 중복되는 코드를 효과적으로 줄여줍니다! 
model을 설정하고 필요한 fields만 적어주면 모델을 참조해서 자동으로 Serializer용 필드를 생성해줍니다.

#### ModelSerializers 클래스 docstrings
A `ModelSerializer` is just a regular `Serializer`, except that:
- A set of default fields are automatically populated.
- A set of default validators are automatically populated.
- Default `.create()` and `.update()` implementations are provided.

The process of automatically determining a set of serializer fields
based on the model fields is reasonably complex, but you almost certainly
don't need to dig into the implementation.

If the `ModelSerializer` class *doesn't* generate the set of fields that
you need you should either declare the extra/differing fields explicitly on
the serializer class, or simply use a `Serializer` class.


### HyperlinkedModelSerializer

5/3 4월분 664.21$ 결제
6/3 5월분 551$ 결제

6/4 4월분 449$ 환불



