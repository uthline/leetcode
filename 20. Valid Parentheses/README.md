## 14. 20. Valid Parentheses
문제 링크: https://leetcode.com/problems/valid-parentheses/

### 문제
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

 1. Open brackets must be closed by the same type of brackets.
 2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

#### Example 1:
```
Input: "()"
Output: true
```
#### Example 2:
```
Input: "()[]{}"
Output: true
```
#### Example 3:
```
Input: "(]"
Output: false
```
#### Example 4:
```
Input: "([)]"
Output: false
```
#### Example 5:
```
Input: "{[]}"
Output: true
```

### 풀이
스택을 이용해야 할 것 만같고, 열고, 닫고 쿵짝을 맞춰보자.
열어 놓고 안닫은 케이스와 열지 않고 닫는 케이스도 확인이 필요.

> open은 stack에 넣고,<br>
> close는 stack에서 꺼내고. 꺼낸거가 이번 close 골호와 쌍인지 확인<br>
> 추가로 stack이 비어져있는 상태인지 확인

### 특이사항
#### 1. 열어 만 놓고 끝나는 문자열
![image](https://user-images.githubusercontent.com/7124469/71188506-70d28280-22c4-11ea-9fe3-d16e27c97fee.png)

이럴경우에는 stack이 empty인지 체크해서 최종 return하자.

#### 2. 열지 않고 닫는 문자열
pop 하기 전에 길이를 체크해서, 열지 않고 닫았는지 확인하자.

### 제출 결과
![image](https://user-images.githubusercontent.com/7124469/71188921-3fa68200-22c5-11ea-8dcc-14b000c3e1bf.png)
