"""
    队列
        - 只允许在前段进行删除操作，在后端进行插入操作。
        先入先出
"""


"""
    队列链表实现
"""
class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, elem):
        p = Node(elem)
        if self.is_empty():
            self.head = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def peek(self):
        if self.is_empty():
            print('Not Found')
        else:
            return self.head.elem

    def print_queue(self):
        print('Queue:')
        temp = self.head
        myqueue = []
        while temp is not None:
            myqueue.append(temp.elem)
            temp = temp.next
        print(myqueue)


"""
    队列数组实现
"""
class Queue(object):
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def enqueue(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    def dequeue(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        self.front -= 1
        self.entries = self.entries[self.front:]
        return dequeued

    def peek(self):
        return self.entries[0]




