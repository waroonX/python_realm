"""
Link:  https://leetcode.com/problems/time-based-key-value-store/description/
Level: Medium
Reason: Failed because of time out issue. Need to increase performance.

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.
"""

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:

    def __init__(self):
        self.root: Node = None

    def put(self, key, value):
        if not self.root:
            self.root = Node(key, value)
            return
        
        current: Node = self.root

        while current:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key, value)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key, value)
                    return
                current = current.right
            else:
                current.value = value
                return
        current = Node(key, value)
        return
    
    def floor_entry(self, key):
        current: Node = self.root
        floor_node: Node = None

        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                floor_node = current
                current = current.right
            else:
                floor_node = current
                break
        
        return floor_node.value if floor_node else None
    
    # def display(self):
    #     """
    #     Public method to initiate the tree display.
    #     """
    #     print("TreeMap Structure:")
    #     if self.root is None:
    #         print("  (empty)")
    #     else:
    #         self._display_recursive(self.root, 0)

    # def _display_recursive(self, node, level):
    #     """
    #     Recursive helper function to print the tree with indentation.
    #     """
    #     if node is not None:
    #         indent = "  " * level
    #         print(f"{indent}Key: {node.key}, Value: {node.value}")
            
    #         # Recursively display the left and right subtrees
    #         self._display_recursive(node.left, level + 1)
    #         self._display_recursive(node.right, level + 1)



class TimeMap:

    def __init__(self):
        self._data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self._data:
            __map = self._data[key]
            __map.put(timestamp, value)
        else:
            __map = TreeMap()
            __map.put(timestamp, value)
        self._data[key] = __map

    def get(self, key: str, timestamp: int) -> str:
        __map: TreeMap = self._data[key]
        val = __map.floor_entry(timestamp)
        return val if val else ""


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set('bar','foo',2)
param_2 = obj.get('bar',3)
print(param_2)

tree_map = TreeMap()
tree_map.put(3, 'abc')
tree_map.put(1, 'cde')
tree_map.put(5, 'cde')
tree_map.put(-1, 'efg')
tree_map.put(7, 'efg')

# tree_map.display()

# print(tree_map.floor_entry(3))
# print(tree_map.floor_entry(4))
# print(tree_map.floor_entry(5))
# print(tree_map.floor_entry(9))
# print(tree_map.floor_entry(0))