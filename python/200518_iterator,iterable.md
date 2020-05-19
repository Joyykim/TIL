Iterable 이란

An object capable of returning its members one at a time. 
자신의 멤버(원소)를 한번에 하나 씩 반환해 줄 수 있는 객체.

Examples of iterables include all sequence types (such as list, str, and tuple) 
and some non-sequence types like dict and file and objects of any classes you define with an __iter__() or __getitem__() method.
sequence 객체는 모두 iterable에 포함된다(list, str, tuple 등).
dict, file과 같은 non-sequence 타입 객체도 iterable이다.
또한 __iter__() 나 __getitem__() 메소드로 정의된 class 는 모두 iterable 하다고 할 수 있다.

Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), ...). 
iterable 은 for loop 말고도, zip(), map()과 같이 sequence 한 특징을 필요로 하는 작업에 유용하게 사용된다. 

When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. 
빌트-인 함수 iter()의 인자로 iterable 객체를 넘겨주면 iterator 객체를 반환한다.

This iterator is good for one pass over the set of values. 
When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. 
The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. 

See also iterator, sequence, and generator.


Iterator 란

An object representing a stream of data. Repeated calls to the iterator’s next() method return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its next() method just raise StopIteration again. Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.