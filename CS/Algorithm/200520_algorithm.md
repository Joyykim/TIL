# Brute Force 
무작위 공격

# Divide and Conquer

기존 문제를 부분 문제로 나누어 해결하고 그 결과를 이용해 기존 문제를 해결하는 접근법.

재귀를 이용해 해결할 수 있다.


# Dynamic Programming

Dynamic Programmingd에 필요한 조건:<br>
1. 최적 부분 구조 (Optimal Substructure)
2. 중복되는 부분 문제 (Overlapping Subproblems)

최적 부분 구조가 있다는 건<br>
부분 문제들의 최적의 답을 이용해서<br>
기존 문제의 최적의 답을 구할 수 있다는 것.<br>
예) 피보나치 수열, 최단 경로 찾기

부분 문제에서 한번 계산한 결과를 기억하고<br>
그 결과를 재활용해 중복되는 부분 문제들을 해결하는 것.<br>
하지만 어떤 부분 문제가 항상 "중복되는 부분 문제"라는 보장은 없다.

Dynamic Programming의 구현 방법
1. Memoization (하향식 접근, 재귀)
2. Tabulation (상향식 접근, 반복문)

Memoization의 단점: Memoization방식으로 재귀를 호출하다 보면 Call stack이 쌓여서 과부하가 일어날 수도 있지만 Tabulation은 반복문을 사용하기 때문에 그럴 위험이 없다.

Tabulation의 단점: 모든 부분 문제를 해결하지 않아도 되는 경우에 Tabulation이 비효율적일 수 있다. Memoization은 필요한 부분 문제만 재귀를 호출하기 때문에 불필요한 연산을 줄일 수 있다.



# Greedy algorithm
