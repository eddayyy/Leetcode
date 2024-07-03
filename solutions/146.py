# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Which data structures to use? 
#   - Hashmap to store the cache
class ListNode:
    def __init__(self, key: int, val:int): 
        self.key = key
        self.val = val
        self.prev, self.next = None, None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.tail, self.head = ListNode(-1, -1), ListNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.dict: return -1 

        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            old_node = self.dict[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.dict[key] = node
        self.add(node) 

        if len(self.dict) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dict[node_to_delete.key]

    def add(self, node: Optional[ListNode]) -> None:
        # Get our second to last element and add the node after it
        previous_end = self.tail.prev
        previous_end.next = node

        # now connect the node to the tail with prev and next 
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node: Optional[ListNode]) -> None: 
        node.prev.next = node.next
        node.next.prev = node.prev
