import time 


#   列表反转
def reverse(l):
    i, j = 0, len(l)-1
    while i<j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    print(l)

# l = [1,2,3,4]
# reverse(l)



"""
    单链表
"""
# 自定义异常
class LinkedListUnderflow(ValueError):
    pass


# 节点类
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        p = self.head
        count = 0
        while p is not None:
            p = p.next
            count += 1
        return count

    def prepend(self, elem):
        self.head = LNode(elem, self.head)

    def pop(self):
        if self.head is None:
            raise LinkedListUnderflow()
        e = self.head.elem
        self.head = self.head.next
        return e

    def append(self, elem):
        node = LNode(elem)
        if self.head is None:
            self.head = node
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node

    def pop_last(self):
        if self.head is None:
            raise LinkedListUnderflow()
        p = self.head
        while p.next.next is not None:
            p = p.next
        p.next = None

    def insert(self, elem, pos):
        node = LNode(elem)
        if pos > self.length():
            raise LinkedListUnderflow('pos too large')
        p = self.head
        if pos == 0:
            self.prepend(elem)
            return
        while pos > 1:
            p = p.next
            pos -= 1
        node.next = p.next
        p.next = node

    def printall(self):
        p = self.head
        while p is not None:
            print(p.elem, end=" ")
            p = p.next

    def filter(self, tar):
        p = self.head
        while p is not None:
            if p.elem == tar:
                yield p.elem
            p = p.next





# l = LList()
# for i in range(5):
#     l.append(i)
#     l.prepend(i)
# l.printall()
#
# print("")
# l.pop()
# l.printall()
#
# print("")
# l.pop_last()
# l.printall()
#
# print("")
# l.insert(99, 0)
# l.insert(99, 5)
# l.printall()
#
# print("")
# res = l.filter(1)
# print('res: ', [i for i in res])
#
# print("")
# print(l.length())



"""
    单链表（加尾节点）
"""
class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self.rear = None

    def prepend(self, elem):
        self.head = LNode(elem, self.head)
        if self.rear is None:
            self.rear = self.head

    def append(self, elem):
        if self.head is None:
            self.head = LNode(elem, self.head)
            self.rear = self.head
        else:
            self.rear.next = LNode(elem)
            self.rear = self.rear.next

    def pop_last(self):
        if self.head is None:
            raise LinkedListUnderflow()
        p = self.head
        if p.next is None:
            e = p.elem
            self.head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self.rear = p


# ll1 = LList1()
# for i in range(5):
#     ll1.append(i)
#     ll1.prepend(i)
# ll1.printall()
#
# print("")
# ll1.pop()
# ll1.pop_last()
# ll1.insert(99,5)
# ll1.printall()



"""
    单向循环链表
"""
class LCList:
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def prepend(self, elem):
        node = LNode(elem)
        if self.rear is None:
            node.next = node
            self.rear = node
        else:
            node.next = self.rear.next
            self.rear.next = node

    def pop(self):
        if self.rear is None:
            raise LinkedListUnderflow()
        else:
            self.rear.next = self.rear.next.next

    def append(self, elem):
        self.prepend(elem)
        self.rear = self.rear.next

    def pop_last(self):
        if self.rear is None:
            raise LinkedListUnderflow()
        else:
            p = self.rear
            while p.next is not self.rear:
                p = p.next
            p.next = self.rear.next
            self.rear = p

    def printall(self):
        if self.is_empty():
            return
        p = self.rear.next
        while True:
            print(p.elem, end=" ")
            if p is self.rear:
                break
            p = p.next


# lc1 = LCList()
# for i in range(5):
#     lc1.append(i)
#     lc1.prepend(i)
# lc1.printall()

# print("")
# lc1.pop()
# lc1.pop_last()
# lc1.printall()



"""
    双向链表
"""

# 双链表类
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev 


# 双向链表
class DList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None 

    def length(self):
        count = 0 
        node = self.head 
        while node is not None:
            node = node.next 
            count += 1 
        return count 

    def prepend(self, elem):
        node = DLNode(elem, None, self.head)
        if self.head is not None:
            node.next.prev = node 
        self.head = node 

    def pop(self):
        if self.head is None:
            raise LinkedListUnderflow()
        e = self.head.elem 
        self.head = self.head.next 
        if self.head is not None:
            self.head.prev = None
        return e 

    def append(self, elem):
        node = DLNode(elem)
        p = self.head 
        if self.head is None:
            self.head = node 
        else:
            while p.next is not None:
                p = p.next 
            p.next = node 
            node.prev = p 

    def pop_last(self):
        if self.head is None:
            raise LinkedListUnderflow()
        p = self.head 
        while p.next.next is not None:
            p = p.next 
        e = p.next.elem 
        p.next.prev = None 
        p.next = None 
        return e 

    def insert(self, pos, elem):
        if pos > self.length():
            raise LinkedListUnderflow('pos too large')
        p = self.head 
        node = DLNode(elem)
        if pos == 0:
            self.prepend(elem)
        else:
            while pos > 1:
                p = p.next 
                pos -= 1
            node.next = p.next 
            p.next.prev = node 
            node.prev = p 
            p.next = node 


    def printall(self):
        p = self.head 
        while p is not None:
            print(p.elem, end=" ")
            p = p.next 


# ddl = DDList()
# for i in range(5):
#     ddl.prepend(i)
#     ddl.append(i)
# ddl.printall()

# print("")
# ddl.pop()
# ddl.pop_last()
# ddl.printall()

# print("")
# ddl.insert(5,99)
# ddl.insert(0,99)
# ddl.printall()


# 加尾指针的双向链表
class DList1(DList):
    def __init__(self):
        DList.__init__(self)
        self.rear = None 

    def prepend(self, elem):
        node = DLNode(elem, None, self.head)
        if self.rear is None:
            self.rear = node 
        else:
            node.next.prev = node 
        self.head = node

    def append(self, elem):
        if self.head is None:
            self.prepend(elem)
        else:
            node = DLNode(elem)
            self.rear.next = node 
            node.prev = self.rear 
            self.rear = self.rear.next 

    def pop_last(self):
        if self.head is None:
            raise LinkedListUnderflow()
        e = self.rear.elem 
        self.rear = self.rear.prev 
        self.rear.next.prev = None 
        self.rear.next = None 
        return e

    def printall(self):
        p = self.head 
        while p is not None:
            print(p.elem, end=" ")
            p = p.next 


# ddl1 = DList1()
# for i in range(5):
#     ddl1.prepend(i)
#     ddl1.append(i)
# ddl1.printall()

# print("")
# print(ddl1.pop())
# print(ddl1.pop_last())
# ddl1.printall()

# print("")
# ddl1.insert(0, 99)
# ddl1.insert(5, 99)
# ddl1.printall()



# 循环双链表
class DCList():
    def __init__(self):
        self.head = None 

    def is_empty(self):
        return self.head is None 

    def length(self):
        p = self.head 
        count = 1
        while p.next is not self.head:
            p = p.next 
            count += 1 
        return count 

    def prepend(self, elem):
        node = DLNode(elem, None, self.head)
        if self.head is None: 
            node.prev = node 
        else:
            p = self.head 
            node.next = p 
            node.prev = p.prev 
            p.prev.next = node 
            p.prev = node 
        self.head = node 

    def pop(self):
        if self.head is None:
            raise LinkedListUnderflow()
        p = self.head 
        e = p.elem 
        self.head = p.next
        p.next.prev = p.prev
        p.prev.next = p.next
        # self.head = p

    def append(self, elem):
        node = DLNode(elem)
        if self.head is None:
            self.prepend(elem)
        else:
            p = self.head 
            node.prev = p.prev 
            node.next = p 
            p.prev.next = node 
            p.prev = node 

    def pop_last(self):
        if self.head is None:
            raise LinkedListUnderflow()
        p = self.head 
        p.prev = p.prev.prev
        p.prev.next = p 

    def printall(self):
        p = self.head 
        while True:
            print(p.elem, end=" ")
            p = p.next
            # time.sleep(1)
            if p is self.head:
                break 


# dc = DCList()
# for i in range(5):
#     dc.prepend(i)
#     dc.append(i)
# dc.printall()

# print("")
# dc.pop()
# dc.pop_last()
# dc.printall()







