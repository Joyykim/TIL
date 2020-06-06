## Advantages using ViewSets and Routers over traditional views

중요
- Routers generate automatic URL patterns and maps every URL to its respective method based on a type of the request.
- We can avoid repetitive code in views. For example, in traditional views we need to have two api views for detail and list. But, we can achive it with a single ViewSet class.
- If we develop a large api and if we don’t use viewset and routers then it will result in more views and urls. It will definitely affect our application(api) maintainablity and development time.

- We can avoid configuring the URL’s with views.
- It deals with a little abstraction but, it can speed up the development process.
- We can also speed up the debugging process as well with a little practice.
- Router generates standardized url patterns.
- We can expect consistent behaviour from viewsets and routers

