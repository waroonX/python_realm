from MyLinkedList import MyLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        f = h = head
        if not f:
            return f
        s = f.next
        if not s:
            return f
        while s:
            f.next = s.next
            s.next = h
            h = s
            s = f.next
        return h

    def reverseList2(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reverseList21(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next  # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head

    def reverseList3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


"""
2  1  3  4  5
"""

if __name__ == "__main__":
    obj = MyLinkedList()
    # obj.addAtTail(1)
    # obj.addAtTail(2)
    # obj.addAtTail(3)
    # obj.addAtTail(4)
    # obj.addAtTail(5)

    print(obj)
    head = Solution().reverseList(obj.head)

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



Approach #1 (Iterative) [Accepted]

Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.

While you are traversing the list, change the current node's next pointer to point to its previous element. Since a node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!

public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}

Complexity analysis

    Time complexity : O(n)O(n)O(n). Assume that nnn is the list's length, the time complexity is O(n)O(n)O(n).

    Space complexity : O(1)O(1)O(1).

Approach #2 (Recursive) [Accepted]

The recursive version is slightly trickier and the key is to work backwards. Assume that the rest of the list had already been reversed, now how do I reverse the front part? Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

Assume from node nk+1 to nm had been reversed and you are at node nk.

n1 → … → nk-1 → nk → nk+1 ← … ← nm

We want nk+1’s next node to point to nk.

So,

nk.next.next = nk;

Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it. This bug could be caught if you test your code with a linked list of size 2.

public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}

Complexity analysis

    Time complexity : O(n)O(n)O(n). Assume that nnn is the list's length, the time complexity is O(n)O(n)O(n).

    Space complexity : O(n)O(n)O(n). The extra space comes from implicit stack space due to recursion. The recursion could go up to nnn levels deep.

"""
