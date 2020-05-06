"""
    节点类
"""
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class DLNode(LNode):
    def __init__(self, elem, next_=None, prev=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


"""
    单链表
"""
class LList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        p = self.head
        c = 0
        while p is not None:
            c += 1
            p = p.next
        return c

    def prepend(self, elem):
        self.head = LNode(elem, self.head)

    def pop(self):
        if self.head is None:
            return
        e = self.head.elem
        self.head = self.head.next
        return e

    def append(self, elem):
        node = LNode(elem)
        p = self.head
        if self.head is None:
            self.head = node
            return
        else:
            while p.next is not None:
                p = p.next
            p.next = node

    def pop_last(self):
        if self.head is None:
            return
        p = self.head
        while p.next.next is not None:
            p = p.next
        e = p.elem
        p.next = None
        return e

    def insert(self, elem, pos):
        node = LNode(elem)
        if pos == 0:
            self.prepend(elem)
        elif pos < self.length():
            p = self.head
            while pos > 0:
                p = p.next
                pos -= 1
            node.next = p.next
            p.next = node
        else:
            raise ValueError('pos out of range')

    def delete(self, pos):
        p = self.head
        while pos > 0:
            pre = p
            p = p.next
            pos -= 1
        pre.next = p.next

    def traversal(self):
        p = self.head
        while p.next is not None:
            print(p.elem, end=" ")
            p = p.next
        print(p.elem, end=" ")

    def reverse(self):
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre


    def swap(self, pos1, pos2):
        if pos1>0 and pos1<self.length() and pos2>0 and pos2<self.length():
            cur1 = self.head
            while pos1 > 0:
                cur1 = cur1.next
                pos1 -= 1
            cur2 = self.head
            while pos2 > 0:
                cur2 = cur2.next
                pos2 -= 1
            cur1.elem, cur2.elem = cur2.elem, cur1.elem
        else:
            raise ValueError('pos1 or pos2 out of range')


def llist_test():
    l = LList()
    for i in range(10):
        l.prepend(i)
        # l.append(i)
    l.traversal()
    print('\nlength:', l.length())
    print('pop:', l.pop())
    print('pop last', l.pop_last())
    l.traversal()

    print("\nInsert:")
    l.insert(99, 5)
    l.traversal()

    print("\nDelete:")
    l.delete(3)
    l.traversal()

    print("\nReverse:")
    l.reverse()
    l.traversal()

    print("\nSwap：")
    l.swap(2,3)
    l.traversal()


# llist_test()



"""
    单向循环链表
"""
class LCList():
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def length(self):
        p = self.head
        c = 0
        while p is not self.rear:
            c += 1
            p = p.next
        return c

    def prepend(self, elem):
        node = LNode(elem)
        if self.head is None:
            self.head = node
            node.next = node
            self.rear = node
        else:
            node.next = self.head
            self.head = node
            self.rear.next = node

    def append(self, elem):
        node = LNode(elem)
        if self.head is None:
            self.head = node
            node.next = node
            self.rear = node
        else:
            node.next = self.rear.next
            self.rear.next = node
            self.rear = node

    def pop(self):
        if self.head is None:
            return
        e = self.head.elem
        self.head = self.head.next
        self.rear.next = self.head
        return e

    def pop_last(self):
        if self.head is None:
            return
        e = self.rear.elem
        p = self.head
        while p.next is not self.rear:
            p = p.next
        p.next = self.head
        self.rear = p
        return e

    def insert(self, elem, pos):
        if pos == 0:
            self.prepend(elem)
        elif pos == self.length():
            self.append(elem)
        else:
            node = LNode(elem)
            p = self.head
            while pos > 1:
                p = p.next
                pos -= 1
            node.next = p.next
            p.next = node

    def delete(self, pos):
        if pos == 0:
            self.pop()
        elif pos == self.length():
            self.pop_last()
        else:
            p = self.head
            while pos:
                pre = p
                p = p.next
                pos -= 1
            pre.next = p.next

    def reverse(self):
        self.rear.next = None
        pre = None
        cur = self.head
        self.rear = cur
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre
        self.rear.next = self.head

    def traversal(self):
        p = self.head
        while p is not self.rear:
            print(p.elem, end=" ")
            p = p.next
        print(p.elem)


def lc_test():
    lc = LCList()
    for i in range(10):
        lc.append(i)

    lc.reverse()
    print('length:', lc.length())
    lc.traversal()

    print('Pop:', lc.pop())
    lc.traversal()

    print('Pop last:', lc.pop_last())
    lc.traversal()

    print('Insert:')
    lc.insert(99, 7)
    lc.traversal()

    print('Delete:')
    lc.delete(6)
    lc.traversal()

    print('Reverse:')
    lc.reverse()
    lc.traversal()


# lc_test()



"""
    双向链表
"""
class DList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        cnt = 0
        while cur.next is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def prepend(self, elem):
        node = DLNode(elem)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            node.next = cur
            cur.prev = node
            self.head = node

    def append(self, elem):
        node = DLNode(elem)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def pop(self):
        if self.head is None:
            raise ValueError('head is None')
        cur = self.head
        e = cur.elem
        cur.next.prev = None
        cur = cur.next
        self.head = cur
        return e

    def pop_last(self):
        if self.head is None:
            raise ValueError('head is None')
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.prev.next = None
        e = cur.elem
        return e

    def insert(self, elem, pos):
        node = DLNode(elem)
        if pos == 0:
            self.prepend(elem)
        elif pos == self.length()+1:
            self.append(elem)
        else:
            cur = self.head
            while pos > 1:
                cur = cur.next
                pos -= 1
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node

    def delete(self, pos):
        cur = self.head
        while pos > 0:
            cur = cur.next
            pos -= 1
        cur.next.prev = cur.prev
        cur.prev.next = cur.next

    def reverse(self):
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            cur.prev = next_node
            pre = cur
            cur = next_node
        self.head = pre

    def swap(self, pos1, pos2):
        p1 = self.head
        p2 = self.head
        pos = max(pos1, pos2)
        while pos > 0:
            if pos1 > 0:
                p1 = p1.next
                pos1 -= 1
            if pos2 > 0:
                p2 = p2.next
                pos2 -= 1
            pos -= 1
        p1.elem, p2.elem = p2.elem, p1.elem

    def traversal(self):
        cur = self.head
        while cur.next is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)


def test_dl():
    dl = DList()
    for i in range(10):
        # dl.append(i)
        dl.prepend(i)
    dl.traversal()
    print('Length:', dl.length())

    print('Pop:', dl.pop())
    dl.traversal()

    print('Pop last:', dl.pop_last())
    dl.traversal()

    print('Insert:')
    dl.insert(99, 5)
    dl.traversal()

    print('Delete:')
    dl.delete(3)
    dl.traversal()

    print('Reverse:')
    dl.reverse()
    dl.traversal()

    print('Swap:')
    dl.swap(3, 5)
    dl.traversal()


# test_dl()



"""
    双向循环链表
"""
class DCLList():
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        cnt = 0
        while cur is not self.rear:
            cnt += 1
            cur = cur.next
        return cnt

    def prepend(self, elem):
        node = DLNode(elem)
        if self.head is None:
            self.head = node
            self.rear = node
            self.head.prev = self.rear
            self.rear.next = self.head
        else:
            node.next = self.head
            node.prev = self.rear
            self.head.prev = node
            self.rear.next = node
        self.head = node

    def traversal(self):
        cur = self.head
        while cur is not self.rear:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def append(self, elem):
        node = DLNode(elem)
        if self.head is None:
            self.head = node
            self.rear = node
            node.prev = self.rear
            node.next = self.head
        else:
            self.rear.next = node
            node.prev = self.rear
            self.head.prev = node
            node.next = self.head
            self.rear = node

    def pop(self):
        cur = self.head
        if self.head is None:
            raise ValueError('head is None')
        e = cur.elem
        cur.next.prev = self.rear
        self.rear.next = cur.next
        self.head = cur.next
        return e

    def pop_last(self):
        if self.head is None:
            raise ValueError('head is None')
        e = self.rear.elem
        self.rear.prev.next = self.head
        self.head.prev = self.rear.prev
        self.rear = self.rear.prev
        return e

    def insert(self, elem, pos):
        node = DLNode(elem)
        if pos == 0:
            self.prepend(elem)
        elif pos == self.length()+1:
            self.append(elem)
        else:
            cur = self.head
            while pos > 1:
                cur = cur.next
                pos -= 1
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node

    def delete(self, pos):
        if pos == 0:
            self.pop()
        elif pos == self.length()+1:
            self.pop_last()
        else:
            cur = self.head
            while pos > 0:
                cur = cur.next
                pos -= 1
            cur.next.prev = cur.prev
            cur.prev.next = cur.next

    def reverse(self):
        pass

    def swap(self):
        pass


def dcl_test():
    dcl = DCLList()
    print('length:', dcl.length())

    for i in range(10):
        # dcl.prepend(i)
        dcl.append(i)
    dcl.traversal()

    print('length:', dcl.length())

    print('Pop:', dcl.pop())
    dcl.traversal()

    print('Pop last', dcl.pop_last())
    dcl.traversal()

    print('Insert:', dcl.insert(99, 0))
    dcl.traversal()

    print('Delete:')
    dcl.delete(5)
    dcl.traversal()


dcl_test()














