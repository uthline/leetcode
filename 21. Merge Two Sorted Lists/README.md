## 21. Merge Two Sorted Lists
문제 링크: https://leetcode.com/problems/merge-two-sorted-lists/

### 문제
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

#### Example:
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

## 풀이
* 처음엔 하나를 다른 하나에 하나씩 삽입한다는 느낌으로 풀려고 했는데, 머리가 굳었는지... 못풀겠다.
* 그쟝 직관적으로, 두개의 list를 모두 비울때까지 새로운 node에 붙여넣는 방식으로 풀었다.
* 소스에서 c는 만들지 않아도 되지만, 소스를 줄이기 위해서 node를 만들고 next를 return하는 방식으로 풀었다.

### 제출 결과
![image](https://user-images.githubusercontent.com/7124469/71522240-2d50c780-2907-11ea-9730-c28a0dcbbd71.png)




