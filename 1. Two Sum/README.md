## 1. Two Sum
문제 링크: https://leetcode.com/problems/two-sum/

### 문제
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

#### Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

### 풀이
list의 두개의 합이 target가 같다것을 바꿔서 생각하면 list에다 target을 새 list에 원래 list의 값이 있으면 그것 두개가 pair로 return이 되면 된다.

```python
a=[2, 7, 11, 15]
b=9-a=[2, 7, -2, -6]
```
a에도 있고 b에도 있는 값을 return

## 제출 결과
![image](https://user-images.githubusercontent.com/7124469/71516977-4baac900-28ef-11ea-8f5f-6888fc92fab9.png)


