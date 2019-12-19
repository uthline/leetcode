## 7. Reverse Integer
문제 링크: https://leetcode.com/problems/reverse-integer/

### 문제
Given a 32-bit signed integer, reverse digits of an integer.

#### Example 1:
```
Input: 123
Output: 321
```
#### Example 2:
```
Input: -123
Output: -321
```
#### Example 3:
```
Input: 120
Output: 21
```
#### Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

### 풀이
주요 로직은 아래와 같다.
> **y = y * 10 + d**<br>
> **d = x % 10**<br>
> **x가 0이 아닐때까지 반복**

### 특이사항
#### 1. 10을 그냥 나누면 float로 인식
int()로 type을 지정해주자.

#### 2. python에서 음수값을 modulo연산으로 나머지를 구하면 이상합 값이 출력된다.
Ex) -123 % 10 = 7
그래서, 부호를 저장하고 입력값을 절대값을 취해서 계산.

#### 3. 부가사항
문제에 integer range를 제한하는 부분이 있어서, 추가로 max, min으로 조건을 걸었다.
* 링크: https://leetcode.com/submissions/detail/287112502/

## 제출 결과
![image](https://user-images.githubusercontent.com/7124469/71180259-2269b780-22b5-11ea-91c4-afbcc3138302.png)
