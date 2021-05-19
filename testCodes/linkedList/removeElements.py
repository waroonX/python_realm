from MyLinkedList import MyLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        f = head
        while f and f.next:
            while f.next and f.next.val == val:
                f.next = f.next.next
            f = f.next
        return head


if __name__ == "__main__":
    obj = MyLinkedList()
    t = [6, 6, 1, 2, 6, 6, 6, 6, 6, 3, 4, 5, 6]
    # t = []
    # t = [7, 7, 7, 7]
    for e in t:
        obj.addAtTail(e)

    print(obj)
    head = Solution().removeElements(obj.head, 2)

    t = []

    while head:
        t.append(str(head))
        head = head.next
    print(t)

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

   Hide Hint #1  
Maintain two pointers and update one with a delay of n steps.
"""
