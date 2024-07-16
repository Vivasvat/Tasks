from typing import Any

l1 = [2,4,3]
l2 = [5,6,4]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode со значением {self.val}"

    def __iter__(self):
        item = self
        while item is not None:
            yield item
            if item.next:
                item = item.next
            else:
                break

def Number(pointer: ListNode) -> int:
    ptr = pointer
    string_int=""
    while ptr is not None:
        strtmp=str(ptr.val)
        string_int+=strtmp
        ptr = ptr.next
    return string_int

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number1=Number(l1)
        number2=Number(l2)
        number1=number1[::-1]
        number2=number2[::-1]
        result = str(int(number1)+int(number2))
        result = result[::-1]

        head = cur = ListNode(0)

        for j in result:
            cur.next = ListNode(j)
            cur = cur.next
        return head.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
itersol = sol.addTwoNumbers(l1, l2)
for i in sol.addTwoNumbers(l1, l2):
    print(i)