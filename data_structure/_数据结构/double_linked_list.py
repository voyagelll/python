"""
    双链表
"""
class Node(object):
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def get_length(self):
        cur = self.head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        return length

    def travel(self):
        cur = self.head
        while cur:
            print(cur.item, end=" ")
            cur = cur.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            # print(cur.item)
            while cur.next is not None:
                cur = cur.next
            # print(cur.item)
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        node = Node(item)
        cur = self.head
        while pos:
            cur = cur.next
            pos -= 1
        cur.next.prev = node
        node.next = cur.next
        cur.next = node
        node.prev = cur

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self.head
            if cur.item == item:
                if cur.next is None:
                    self.head = None
                else:
                    cur.next.prev = None
                    self.head = cur.next
            while cur is not None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next


dll = DoubleLinkedList()
dll.append(1)
dll.append(1)
dll.append(1)
dll.add(0)
dll.add(0)
dll.add(0)
dll.insert(3,3)
dll.insert(3,3)
dll.insert(3,3)
dll.travel()

print("")
print(dll.search(3))
print(dll.search(4))

dll.remove(3)
dll.remove(3)
dll.remove(3)
dll.travel()
