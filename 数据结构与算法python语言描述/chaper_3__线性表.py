# 单链表的实现

class LNode:
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_


# 自定义异常 
class LinkedListUnderflow(ValueError):
	pass 


# LList 类定义，初始化函数和简单操作
"""
	单链表
"""
class LList:
	def __init__(self):
		self.head = None 

	def is_empty(self):
		return self.head is None 

	def prepend(self, elem):
		self.head = LNode(elem, self.head)

	def pop(self):
		if self.head is None:
			raise LinkedListUnderflow('in pop')
		e = self.head.elem 
		self.head = self.head.next 

	def append(self, elem):
		if self.head is None:
			self.head = LNode(elem)
			return 
		p = self.head 
		while p.next is not None:
			p = p.next
		p.next = LNode(elem)

	def pop_last(self):
		if self.head is None:
			raise LinkedListUnderflow()
		p = self.head 
		if p.next is None:   # 表中只有一个元素
			e = p.elem 
			self.head = None 
			return e
		while p.next.next is not None:
			p = p.next 
		e = p.next.elem 
		p.next = None 
		return e 

	def insert(self, pos, elem):
		if self.head is None and pos == 0:
			self.head = LNode(elem)
		p = self.head 
		node = LNode(elem)
		if pos == 0:
			node.next = p 
			self.head = node 
		else:
			while pos > 1:
				p = p.next
				pos -= 1 
			node.next = p.next
			p.next = node 

	def delete(self, pos):
		p = self.head 
		while pos > 1:
			p = p.next 
			pos -= 1
		p.next = p.next.next


	def find(self, elem):
		p = self.head 
		while p is not None:
			if p.elem == elem:
				return elem 
			p = p.next 
		return 

	def printall(self):
		p = self.head 
		while p is not None:
			print(p.elem, end=" ")
			p = p.next 

	def for_each(self, proc):  # 遍历
		p = self.head 
		while p is not None:
			proc(p.elem)
			p = p.next 

	def elements(self):  # 迭代
		p = self.head 
		while p is not None:
			yield p.elem 
			p = p.next 




l1 = LList()
for i in range(10):
	l1.prepend(i)
for i in range(11, 20):
	l1.append(i)
# l1.printall()

# l1.for_each(print)

# for i in l1.elements():
# 	print(i)

# l1.insert(5, 111)
# l1.printall()
# print("")

# l1.delete(5)
# l1.printall()



"""
	单链表变形(加尾指针)
"""
class LList1(LList):
	def __init__(self):
		LList.__init__(self)
		self.rear = None 

	def prepend(self, elem):
		if self.head is None:
			self.head = LNode(elem, self.head)
			self.rear = self.head 
		else:
			self.head = LNode(elem, self.head)

	def append(self, elem):
		if self.head is None:
			self.head = LNode(elem, self.head)
			self.rear = self.head 
		else:
			self.rear.next = LNode(elem)
			self.rear = self.rear.next 

	def pop_last(self):
		if self.head is None:
			raise LinkedListUnderflow('in pop_last')
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


# l1 = LList1()
# l1.append(99)
# for i in range(11, 20):
# 	l1.append(i)

# l1.printall()
# print('')
# l1.pop()
# l1.pop_last()
# l1.printall()



"""
	循环单链表
"""
class LCist:
	def __init__(self):
		self.head = None 

	def is_empty(self):
		return self.head is None 

	def prepend(self, elem):
		p = LNode(elem)
		if self.head is None:
			p.next = p 
			self.head = p 
		else:
			
