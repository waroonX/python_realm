"""

link: From Hackerrank grid Challenge
level: intermediate
score: 0


"""

class SinglyLinkedListNode:
    
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next
        
def print_link(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()
        
def mergeLists(head1, head2):
    link1, link2 = (head1, head2) if head1.data <= head2.data else (head2, head1)
    orig = link1
    while link1 and link1.next:
        data = link2.data
        if link1.data <= data <= link1.next.data:
            mid = SinglyLinkedListNode(data)
            mid.next = link1.next
            link1.next = mid
            link2 = link2.next
            if not link2:
                break
        link1 = link1.next
    if link2:
        link1.next = link2
    return orig
        
        

def create_link(arr):
    ref = None
    for elem in arr[::-1]:
        ref = SinglyLinkedListNode(elem, ref)
    return ref
    
if __name__ == "__main__":
    arr1 = [2, 3, 7, 9, 9]
    arr2 = [1, 2, 5, 6]
    
    print_link(mergeLists(create_link(arr1), create_link(arr2)))