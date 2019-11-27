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

	def is_empty(self):
		return self.__head == None

	def length(self):
		if self.__head is None:
			return 0 
		cur = self.__head 
		count = 1
		while cur.next is not None:
			cur = cur.next 
			count += 1
		return count 

	def travel(self):
		cur = self.__head 
		# print(self.__head.elem)
		while cur is not None:
			print(cur.elem, end=" ")
			cur = cur.next 
		print("")

	def add(self, item):
		"""头部添加元素"""
		node = Node(item)
		node.next = self.__head 
		self.__head = node 

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head = node 
		else:
			cur = self.__head 
			while cur.next is not None:
				cur = cur.next 
			cur.next = node 

	def insert(self, pos, item):
		if pos == 0:
			self.add(item)
		elif pos > self.length()-1:
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
		cur = self.__head 
		pre = None 
		while cur is not None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next 
				else:
					pre.next = cur.next 
				break
			else:
				pre = cur 
				cur = cur.next 


	def search(self, item):
		cur = self.__head 
		while cur is not None:
			if cur.elem == item:
				return True 
			cur = cur.next 
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