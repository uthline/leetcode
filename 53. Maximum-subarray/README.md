## 53. Maximum Subarray
문제 링크: https://leetcode.com/problems/maximum-subarray/

### 문제
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#### Example:
```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

#### Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

### 풀이
* 음수는 더해져도 도움이 안됨.
* 최종적으로 최대합을 리턴
* 현재까지 합이 음수이면, 다음의 입력이 최대합의 후보.
* 현재까지 합의 양수면, 다음의 입력을 현재까지 합에 더해보자.
* 지금까지 최대합과 현재까지 합을 비교

### 분할정복으로? 
* 분할영역을 합해서 커지면 더하고, 안커지면 더하지말고.
* 더했다는 것도 결국엔 sum의 값

### 제출 결과
![image](https://user-images.githubusercontent.com/7124469/74692757-00949e80-522c-11ea-9f26-1ca37989a78d.png)
  