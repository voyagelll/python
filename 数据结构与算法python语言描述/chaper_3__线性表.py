
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




lc1 = LCList()
for i in range(5):
    lc1.append(i)
    lc1.prepend(i)
lc1.printall()

print("")
lc1.pop()
lc1.pop_last()
lc1.printall()