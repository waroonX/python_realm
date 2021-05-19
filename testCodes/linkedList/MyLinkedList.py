class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next: Node = next

    def __str__(self) -> str:
        return f"Node: {self.val}"


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        head = self.head
        while index > 0 and head:
            head = head.next
            index -= 1
        if not head or index != 0:
            return -1
        else:
            return head.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail = Node(val)
        head = self.head
        if not head:
            self.head = tail
        else:
            while head.next:
                head = head.next
            head.next = tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        head = self.head
        if not head or not index:
            self.addAtHead(val)
            return None
        new_node = Node(val)
        while index - 1 > 0 and head.next:
            head = head.next
            index -= 1
        if index != 1:
            return None
        elif not head.next:
            head.next = new_node
        else:
            new_node.next = head.next
            head.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        head = self.head
        if not head:
            return None
        elif not index:
            self.head = head.next
        index -= 1
        while index > 0 and head.next:
            head = head.next
            index -= 1
        if index != 0:
            return None
        elif head.next:
            head.next = head.next.next
        else:
            head.next = None

    def __str__(self) -> str:
        if not self.head:
            return "[]"
        else:
            head = self.head
            s = []
            while head:
                s.append(str(head))
                head = head.next
            return "[" + ", ".join(s) + "]"


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtTail(4)
    obj.addAtTail(5)

    # print(obj.get(2))
    # print(obj.get(3))
    print(obj)
    obj.addAtIndex(5, -1)
    print(obj)
    obj.deleteAtIndex(6)
    print(obj)
    # param_1 = obj.get(index)
    # obj.addAtHead(val)
    # obj.addAtTail(val)
    # obj.addAtIndex(index, val)
    # obj.deleteAtIndex(index)


"""
class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def getLength(self): 
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
            
        return count

    def get(self, index):
        length = self.getLength()
        if index+1 > length or index < 0:
            return -1
        elif index == 0:
            return self.head.val
        else:
            count = 0
            iterator = self.head
            while iterator.next:
                count += 1
                if count == index:
                    return iterator.next.val
                    break
                iterator = iterator.next
        

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        iterator.next = new_node

    def addAtIndex(self, index, val):
        length = self.getLength()
        if index > length:
            return 'index is invalid'
        if index == 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            iterator = self.head
            while iterator:
                count += 1
                if count == index:
                    new_node = Node(val)
                    new_node.next = iterator.next 
                    iterator.next  = new_node

                iterator = iterator.next
        

    def deleteAtIndex(self, index):
        iterator = self.head
        length = self.getLength()
        if index > length:
            return 'index is invalid'
        elif index == 0:
            self.head = iterator.next
        else:
            count = 0
            
            while iterator.next:
                count += 1
                if count == index:
                    iterator.next = iterator.next.next
                    break

                iterator = iterator.next

"""
