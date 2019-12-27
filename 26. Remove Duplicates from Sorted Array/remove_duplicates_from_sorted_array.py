"""
문제 링크
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        leng = 0

        for n in range(1, len(nums)):
            if nums[leng] != nums[n]:
                leng += 1
                nums[leng] = nums[n]

        return leng + 1


if __name__ == '__main__':
    ans = Solution()
    print(ans.removeDuplicates([1, 1, 2]))
    print(ans.removeDuplicates([1, 2, 3]))
    print(ans.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(ans.removeDuplicates([1, 2, 2]))
    print(ans.removeDuplicates([1, 1, 1]))
    print(ans.removeDuplicates([]))
