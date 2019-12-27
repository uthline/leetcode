"""
문제 링크
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        n = self
        while n != None:
            print(n.val, end='->')
            n = n.next
        print()

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = c = ListNode(0)

        while l1 or l2:
            if l1 is None:
                c.next = l2
                return node.next
            elif l2 is None:
                c.next = l1
                return node.next
            elif l1.val >= l2.val:
                t = l2
                l2 = l2.next
                t.next = None
                c.next = t
                c = c.next
            else:
                t = l1
                l1 = l1.next
                t.next = None
                c.next = t
                c = c.next

        return node.next


if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(4)
    b1 = ListNode(1)
    b2 = ListNode(3)
    b3 = ListNode(4)

    a1.next = a2
    a2.next = a3
    b1.next = b2
    b2.next = b3

    ans = Solution()
    ans.mergeTwoLists(a1, b1).print()

    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    b1 = ListNode(4)
    b2 = ListNode(5)
    b3 = ListNode(6)

    a1.next = a2
    a2.next = a3
    b1.next = b2
    b2.next = b3

    ans.mergeTwoLists(a1, b1).print()

    a1 = ListNode(4)
    a2 = ListNode(5)
    a3 = ListNode(6)
    b1 = ListNode(1)
    b2 = ListNode(2)
    b3 = ListNode(3)

    a1.next = a2
    a2.next = a3
    b1.next = b2
    b2.next = b3

    ans.mergeTwoLists(a1, b1).print()
