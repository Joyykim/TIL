Jackson은 java의 json 프로세싱 라이브러리로 유명하다.
Jackson에는 ObjectMapper 클래스가 있는데 POJO(Plain Old Java Object)를 JSON으로 변환하거나, 반대로 JSON을 POJO로 변환한다.

우아한테크코스에서 간단한 MVC프레임워크를 구현하는 미션을 진행하던중 ObjectMapper를 사용하게 되었다.
나는 ObjectMapper를 싱글턴 객체로 만들어 재사용해도 될지 고민이 생겼다. 내가 만드는 프레임워크는 멀티 쓰레드로 동작하기 때문에 Thread-safe한지가 중요했다.

# ObjectMapper는 Thread-safe 한가?

일단 ObjectMapper 인스턴스는 불변 객체가 아니다. 공식문서에 따르면 ObjectMapper는 ObjectReader, ObjectWriter 를 생성하는 팩토리처럼 동작한다고 한다. Mapper 필드에는 read, write 기능을 위한 여러가지 Configuration 객체들을 필드로 가지고 있는데, 대부분이 final이 아니며 setConfig(), setDateFormat() 등의 메서드들을 통해 설정을 바꿀 수 있다.
> ObjectMapper also acts as a factory for more advanced ObjectReader and ObjectWriter classes.

[Jackson 공식문서](https://fasterxml.github.io/jackson-databind/javadoc/2.7/com/fasterxml/jackson/databind/ObjectMapper.html)에서는 Mapper 객체는 configuring 메서드(setConfig, setDateFormat 등)가 실행중이 아닐 때만 read, write 요청이 Thread-safe 하다고 한다.
> Mapper instances are fully thread-safe provided that ALL configuration of the instance occurs before ANY read or write calls.

> ObjectMapper itself is only thread-safe when configuring methods (such as this one) are NOT called.

## ObjectReader, ObjectWriter
ObjectMapper는 ObjectReader, ObjectWriter 객체를 생성할 수 있는데, 이 두 클래스의 인스턴스는 외부에서 동기화작업을 해주지 않아도 되는 Thread-safe한 불변 객체다.
ObjectMapper의 Configuration에 따라 writer(), reader() 메서드로 두 객체를 만들 수 있다.
ObjectMapper에서 Reader,Writer를 생성하는 작업은 값싼 연산이기 때문에 만약 Reader,Writer 객체를 재사용하고 싶지도 않고 메모리를 차지하는게 싫다면, Mapper만 가지고 있고 필요할 때만 Mapper에서 생성해도 괜찮다고 한다.

기능적으로도 Mapper와 Reader,Writer는 차이가 있다. 
ObjectReader.readValues(InputStream), ObjectWriter.writeValues(OutputStream) 는 훨씬 긴 시퀀스의 입출력을 처리할 수 있는데, Mapper에는 이 메서드가 없다.
> Note that although most read and write methods are exposed through this class, some of the functionality is only exposed via ObjectReader and ObjectWriter: specifically, reading/writing of longer sequences of values is only available through ObjectReader.readValues(InputStream) and ObjectWriter.writeValues(OutputStream).

# ObjectMapper는 Multi-Thread 성능 이슈

검색 중 ObjectMapper를 멀티 쓰레드에서 사용하지 마라는 근거 중 lock으로 인한 성능저하가 있다는 글을 보았다. 그런데 누군가는 전혀 lock이 없다고 의견이 갈려서 찾아보니 예전 버전에는 lock 이슈가 있었다는걸 발견했다. 아래는 ObjectMapper 내부의 synchronized 블록으로 인한 멀티쓰레드 성능이슈를 발견하고 해결한 분이 그 과정을 작성한 글이다.
https://medium.com/feedzaitech/when-jackson-becomes-a-parallelism-bottleneck-f1440a50b429

https://github.com/FasterXML/jackson-core/issues/349
해당 이슈에선 2.8.7 버전부터 개선되었다고 한다. 확인해보니 정말 해당 버전부터 synchronized 블록이 사라졌다.

**2.8.6**

<img width="754" alt="스크린샷 2021-09-24 오후 7 27 10" src="https://user-images.githubusercontent.com/56679885/134709419-8b9b368a-8006-400c-858a-2d3b3d6bf901.png">

**2.8.7**

<img width="801" alt="스크린샷 2021-09-24 오후 7 26 41" src="https://user-images.githubusercontent.com/56679885/134709442-afb8e96c-a04a-4a61-beb4-d21b2918e1ad.png">
