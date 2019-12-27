"""
문제 링크
https://leetcode.com/problems/two-sum/
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(0, len(nums)):
            d = target - nums[i]
            if maps.get(d) is not None:
                return [i, maps[d]]
            else:
                maps[nums[i]] = i

if __name__ == '__main__':
    ans = Solution()
    print(ans.twoSum([2, 7, 11, 15], 9))
