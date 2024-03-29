# Cache

참조: https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching<br>
https://web.dev/http-cache/<br>
https://developer.mozilla.org/ko/docs/Web/HTTP/Caching

## 브라우저 호환성

사실 HTTP Cache는 단일 API가 아닙니다. Cache-Control, ETag, Last-Modified 등 여러 API가 모여서 HTTP 캐싱을 구현하는 겁니다. 그 API들은 모든 브라우저에서 지원합니다.

## HTTP Cache를 사용하는 이유

네트워크를 통해 무언가를 가져오는 작업은 느린 동시에 비용도 많이 듭니다. 크기가 큰 응답은 클라이언트와 서버 사이에 많은 왕복을 필요로 하므로, 응답을 사용할 수 있게 되어 브라우저가 처리할 수 있게 되는 시기가 지연되고 방문자에 대한 데이터 비용도 발생합니다. 따라서 이전에 가져온 리소스를 캐시했다가 재활용할 수 있는 기능은 성능 최적화에 있어 중요한 측면입니다.

좋은 소식은, 모든 브라우저에 HTTP 캐시 구현이 포함되어 있다는 것입니다. 여러분이 해야 할 일은 하나뿐입니다. 각 서버 응답이 올바른 HTTP 헤더 지시문을 제공하여 브라우저에 해당 브라우저가 응답을 캐시할 시점과 기간을 지시하는지 확인하기만 하면 됩니다.

![Example](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/images/http-request.png)

서버가 응답을 반환할 때는 응답의 콘텐츠 유형, 길이, 캐싱 지시문, 유효성 검사 토큰 등을 설명하는 HTTP 헤더 모음도 방출합니다. 예를 들어, 위의 교환에서 서버는 1024바이트의 응답을 반환하고, 클라이언트에 최대 120초 동안 이를 캐시하도록 지시하고, 응답이 만료된 후 리소스가 수정되었는지 확인하는 데 사용할 수 있는 유효성 검사 토큰('x234dff')을 제공합니다.

## How the HTTP Cache works

All HTTP requests that the browser makes are first routed to the browser cache to check whether there is a valid cached response that can be used to fulfill the request. If there's a match, the response is read from the cache, which eliminates both the network latency and the data costs that the transfer incurs.

The HTTP Cache's behavior is controlled by a combination of request headers and response headers. In an ideal scenario, you'll have control over both the code for your web application (which will determine the request headers) and your web server's configuration (which will determine the response headers).

Check out MDN's HTTP Caching article for a more in-depth conceptual overview.

https://developer.mozilla.org/ko/docs/Web/HTTP/Caching