class Node(object):
	def __init__(self, item):
		self.elem = item 
		self.next = None 
		self.prev = None


class DoubleLinkList(object):
	def __init__(self, node=None):
		self.__head = node 

	def is_empty(self):
		return self.__head is None 

	def length(self):
		cur = self.__head 
		count = 0 
		while cur:
			count += 1
			cur = cur.next 
		return count 

	def travel(self):
		cur = self.__head 
		while cur is not None:
			print(cur.elem, end=" ")
			cur = cur.next
		print("")

	def add(self, item):
		node = Node(item)
		node.next = self.__head
		self.__head = node 
		# node.next.prev = node

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head 
			while cur.next is not None:
				cur = cur.next 
			cur.next = node 
			node.prev = cur

	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			count = 0 
			cur = self.__head
			while count<pos:
				count += 1 
				cur = cur.next
			node = Node(item)
			node.next = cur
			node.prev = cur.prev
			cur.prev.next = node
			cur.prev = node

	def search(self, item):
		cur = self.__head
		while cur:
			if cur.elem == item:
				return True
			cur = cur.next
		return False

	def remove(self, item):
		cur = self.__head
		while cur is not None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next
					if cur.next:
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else:
				cur = cur.next


if __name__ == '__main__':
	ll = DoubleLinkList()
	print(ll.is_empty())
	print(ll.length())

	ll.append(1)
	print(ll.is_empty())
	print(ll.length())
	ll.travel()

	ll.append(2)
	ll.append(3)
	ll.travel()

	ll.add(100)
	ll.travel()

	ll.insert(0, 9)
	ll.insert(4, 10)
	ll.travel()

	print(ll.search(3))

	ll.remove(1)
	ll.travel()

	ll.remove(9)
	ll.remove(3)
	ll.travel()
