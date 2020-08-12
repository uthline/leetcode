"""
문제 링크
https://leetcode.com/problems/maximum-subarray/
"""
from typing import List

class Solution:
    def justSum(self, nums: List[int]) -> int:
        def sum_devide_and_conquer(left: int, right: int):
            sum = 0
            if left == right:
                return nums[left]

            pivot = int((left + right) / 2)
            print(pivot, left, right, nums[left:right+1])
            left_sum = sum_devide_and_conquer(left, pivot)
            right_sum = sum_devide_and_conquer(pivot+1, right)

            return left_sum + right_sum

        return sum_devide_and_conquer(0, len(nums)-1)

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = nums[i] if curr_sum < 0 else curr_sum + nums[i]
            max_sum = max(curr_sum, max_sum)

        return max_sum

    def devide(self, nums: List[int]) -> int:
        def conditional_sum(left: int, right: int, lr: str):
            if left == right:
                return nums[left]

            pivot = int((left + right) / 2)
            left_sum = conditional_sum(left, pivot, 'left')
            right_sum = conditional_sum(pivot+1, right, 'right')

            sum = left_sum + right_sum
            # print("{} {} {} nums:{} left:{} right:{}".format(left, right, lr, nums[left:right + 1], nums[left:pivot+1], nums[pivot+1:right+1]))
            return sum

        return conditional_sum(0, len(nums)-1, None)

if __name__ == '__main__':
    ans = Solution()

    print(ans.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(ans.maxSubArray([-1, 0, 2, -1, 2, -1]))
    print(ans.maxSubArray([-3, -2, -3,-1]))
