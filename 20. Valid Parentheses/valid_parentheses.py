"""
문제 링크
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_pair = {'(': ')', '[': ']', '{': '}'}
        open_parentheses = ['(', '[', '{']
        close_parentheses = [')', ']', '}']

        for c in s:
            if c in open_parentheses:
                stack.append(c)
            if c in close_parentheses:
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if parentheses_pair[pop] != c:
                    return False

        if len(stack) != 0:
            return False
        return True


if __name__ == '__main__':
    ans = Solution()
    ans.isValid("()")
    ans.isValid("()[]{}")
    ans.isValid("(]")
    ans.isValid("([)]")
    ans.isValid("{[]}")

    ans.isValid("[")
    ans.isValid("]")
