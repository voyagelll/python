# class Node(object):
# 	def __init__(self, elem):
# 		self.elem = elem
# 		self.next = None
#
#
# class SingleLinkList(object):
# 	"""
# 		单链表
# 	"""
# 	def __init__(self, node=None):
# 		self.__head = node
#
# 	def is_empty(self):
# 		return self.__head == None
#
# 	def length(self):
# 		if self.__head is None:
# 			return 0
# 		cur = self.__head
# 		count = 1
# 		while cur.next is not None:
# 			cur = cur.next
# 			count += 1
# 		return count
#
# 	def travel(self):
# 		cur = self.__head
# 		# print(self.__head.elem)
# 		while cur is not None:
# 			print(cur.elem, end=" ")
# 			cur = cur.next
# 		print("")
#
# 	def add(self, item):
# 		"""头部添加元素"""
# 		node = Node(item)
# 		node.next = self.__head
# 		self.__head = node
#
# 	def append(self, item):
# 		node = Node(item)
# 		if self.is_empty():
# 			self.__head = node
# 		else:
# 			cur = self.__head
# 			while cur.next is not None:
# 				cur = cur.next
# 			cur.next = node
#
# 	def insert(self, pos, item):
# 		if pos == 0:
# 			self.add(item)
# 		elif pos > self.length()-1:
# 			self.append(item)
# 		else:
# 			cur = self.__head
# 			while pos > 1:
# 				cur = cur.next
# 				pos -= 1
# 			node = Node(item)
# 			node.next = cur.next
# 			cur.next = node
#
# 	def remove(self, item):
# 		cur = self.__head
# 		pre = None
# 		while cur is not None:
# 			if cur.elem == item:
# 				if cur == self.__head:
# 					self.__head = cur.next
# 				else:
# 					pre.next = cur.next
# 				break
# 			else:
# 				pre = cur
# 				cur = cur.next
#
#
# 	def search(self, item):
# 		cur = self.__head
# 		while cur is not None:
# 			if cur.elem == item:
# 				return True
# 			cur = cur.next
# 		return False
#
#
# if __name__ == '__main__':
# 	ll = SingleLinkList()
# 	print(ll.is_empty())
# 	print(ll.length())
#
# 	ll.append(1)
# 	print(ll.is_empty())
# 	print(ll.length())
#
# 	ll.append(2)
# 	ll.append(3)
# 	ll.travel()
#
# 	ll.add(100)
# 	ll.travel()
#
# 	ll.insert(0, 9)
# 	ll.insert(4, 10)
# 	ll.travel()
#
# 	print(ll.search(3))
#
# 	ll.remove(100)
# 	ll.travel()
#
# 	ll.remove(9)
# 	ll.remove(3)
# 	ll.travel()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """返回链表长度"""
        cur = self.head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count

    def append(self, item):
        """在链表后增加一个元素"""
        if self.is_empty():
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next:
                # print(cur, end=" ")
                cur = cur.next
            cur.next = Node(item)

    def insert(self, pos, item):
        """在指定索引插入元素"""
        node = Node(item)
        cur = self.head
        if pos <= 0:
            node.next = cur
            self.head = node
        else:
            length = self.length()
            if pos > length:
                pos = length
            while pos > 1:
                cur = cur.next
                pos -= 1
            node.next = cur.next
            cur.next = node

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print("")

    def remove(self, pos):
        """移除指定位置元素"""
        cur = self.head
        pre = None
        if pos <= 0:
            self.head = self.head.next
        else:
            while pos > 1:
                pos -= 1
                pre = cur
                cur = cur.next
            pre.next = cur.next

    def reverse(self):
        """翻转链表"""
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre

    def init_list(self, data_list):
        """将列表转为链表"""
        self.head = Node(data_list[0])
        cur = self.head
        for i in data_list[1:]:
            node = Node(i)
            cur.next = node
            cur = cur.next



if __name__ == '__main__':
    ll = Linked_List()
    print(ll.is_empty())
    print(ll.length())
    print(ll.travel())

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll.length())
    ll.travel()

    ll.insert(0, 0)
    ll.insert(2, 10)
    ll.insert(6, 6)
    ll.travel()
    # print(ll.length())

    # ll.remove(2)
    ll.remove(0)
    ll.travel()
    ll.remove(6)
    ll.travel()
    ll.remove(2)
    ll.travel()

    ll.reverse()
    ll.travel()

    l = [99, 99, 99]
    ll.init_list(l)
    ll.travel()
