## 26. Remove Duplicates from Sorted Array
문제 링크: https://leetcode.com/problems/merge-two-sorted-lists/

### 문제
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

#### Example 1:
```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```
#### Example 2:
```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```
#### Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

### 풀이
* 정렬되어 있는 list 이기때문에, 바로 압뒤의 것만 비교하면 동일한 것인지 확인하면서 반복
* 동일하지 않은 것을 발견하였을 경우에만, 배열에 값을 넣어줌.
* 배열의 첫번째는 무조건 유니크하다고 말할 수있다.
* 그 이후 배열에다가 중복되지 않는 값을 넣어주면 된다.

### 특이사항
* reference list임으로 리턴하는 배열이 중복되지 않는 list를 만들어야 한다고 이해했는데, 그건 아니고 그냥 중복되지 않는 값들의 갯수만 return하면 된다. 괜히 어렵게 생각하지 말라.

### 제출 결과
![image](https://user-images.githubusercontent.com/7124469/71524513-4b232a00-2911-11ea-8d0b-09e917dc6b2d.png)


