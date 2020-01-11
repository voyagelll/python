class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """
		单链表
	"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.__head is None:
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        # print(self.__head.elem)
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)
        print("")

    def add(self, item):
        """头部添加元素"""
        cur = self.__head
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            node.next = self.__head
            # 找到尾节点
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            while pos > 1:
                cur = cur.next
                pos -= 1
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            cur = cur.next
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.travel()

    ll.add(100)
    ll.travel()

    ll.insert(0, 9)
    ll.insert(4, 10)
    ll.travel()

    print(ll.search(3))

    ll.remove(100)
    ll.travel()

    ll.remove(9)
    ll.remove(3)
    ll.travel()
