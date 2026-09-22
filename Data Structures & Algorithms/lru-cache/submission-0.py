class DLLNode:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head


    def _add_node(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self._move_to_head(node)

        else:
            new_node = DLLNode(key,value)
            self._add_node(new_node)
            self.cache[key] = new_node

            if len(self.cache) > self.capacity:
                node = self._pop_tail()
                del self.cache[node.key]
        
