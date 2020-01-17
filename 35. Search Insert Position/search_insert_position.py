"""
문제 링크
https://leetcode.com/problems/search-insert-position/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(nums: List[int], start: int, end: int, target: int):
            if start <= end:
                mid = start+end-1 // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binarySearch(nums, mid+1, end, target)
                elif nums[mid] > target:
                    return binarySearch(nums, start, mid-1, target)
            else:
                return start

        return binarySearch(nums, 0, nums.__len__()-1, target)


if __name__ == '__main__':
    ans = Solution()
    print(ans.searchInsert([1, 1, 2], 3))
    print(ans.searchInsert([1, 3, 5, 6], 5))
    print(ans.searchInsert([1, 3, 5, 6], 2))
    print(ans.searchInsert([1, 3, 5, 6], 7))
    print(ans.searchInsert([1, 3, 5, 6], 0))
