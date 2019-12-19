"""
문제 링크
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0] if len(strs) else ""
        pre = ""
        d = 0
        for letter in word:
            for s in strs:
                c = s[d] if len(s) > d else ""
                if c != letter:
                    return pre

            pre = pre + letter
            d = d + 1
        return pre


if __name__ == '__main__':
    ans = Solution()
    ans.longestCommonPrefix(["flower", "flow", "flight"])
    ans.longestCommonPrefix(["dog", "racecar", "car"])

    # https://leetcode.com/submissions/detail/287122249/
    ans.longestCommonPrefix([])

    # https://leetcode.com/submissions/detail/287123259/
    ans.longestCommonPrefix(["aa", "a"])


