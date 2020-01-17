## 35. Search Insert Position
문제 링크: https://leetcode.com/problems/search-insert-position/

### 문제
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

#### Example 1:
```
Input: [1,3,5,6], 5
Output: 2
```

#### Example 2:
```
Input: [1,3,5,6], 2
Output: 1
```

#### Example 3:
```
Input: [1,3,5,6], 7
Output: 4
```

#### Example 4:
```
Input: [1,3,5,6], 0
Output: 0
```

### 풀이
* 정렬되어 있는 Array이야기가 나오면 일단, binary search로 해결하면 빠르겠다 싶음
* binary search면 또, device and conquer로 풀어야하니깐, 반복이 종료되는 조건을 설정해보자.
1. 찾았거나
2. start와 end가 같거나
* 못찾았으면, 현재 index기준으로 오른쪽인지 왼쪽인지 판단해서 재귀적으로 호출.


### 특이사항
* 재귀적으로 호출시, 현재 조사한 값의 index를 넘기지말고, 상황에 맞게 index+1 또는 index-1을 넘겨야한다. 안그러면 무한 호출
* 종료조건을 start와 end가 같을 경우에서 `start<=end`로 변경
* 못찾은 경우는 start의 index를 넘기자.


### 제출 결과
![image](https://user-images.githubusercontent.com/7124469/72574330-fec57b80-390b-11ea-8cf3-73fe55056d51.png)
