"""
문제 링크
https://leetcode.com/problems/reverse-integer/

풀이
주요 로직는 y = y * 10 + d, d = x % 10. x가 0이 아닐때까지 반복.

특이점
1. python에서 음수값을 modulo연산으로 나머지를 구하면 이상합 값이 출력된다.
Ex) -123 % 10 = 7
그래서, 부호를 저장하고 입력값을 절대값을 취해서 계산.

2. 10을 그냥 나누면 float로 인식.
int()로 변형해 줬다.

부가사항
문제에 integer range를 제한하는 부분이 있어서, 추가로 max, min으로 조건을 걸었다.
링크: https://leetcode.com/submissions/detail/287112502/
"""


class Solution:
    def reverse(self, x: int) -> int:
        max = (2 ** 31) - 1
        min = (2 ** 31) * -1
        y = 0
        s = -1 if x < 0 else 1
        x = abs(x)
        while x:
            d = x%10
            y = y*10 + d
            x = int(x/10)
        y = y*s
        if y > max or y < min:
            return 0
        else:
            return y


if __name__ == "__main__":
    a = Solution()
    a.reverse(123)
    a.reverse(-123)
    a.reverse(120)

    """ submit할 때 fail한 추가 input. https://leetcode.com/submissions/detail/287112502/
    """
    a.reverse(1534236469)
