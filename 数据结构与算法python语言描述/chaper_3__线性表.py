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

	def reverse(self):
		p = None
		while self.head is not None:
			q = self.head
			self.head = q.next
			q.next = p
			p = q
		self.head = p

	def sort1(self):    # 插入排序，方式：交换两个元素的位置
		if self.head is None:
			return
		crt = self.head.next
		while crt is not None:
			x = crt.elem
			p = self.head
			while p is not crt and p.elem <= x:
				p = p.next
			while p is not crt:
				y = p.elem
				p.elem = x
				x = y
				p = p.next
			crt.elem = x
			crt = crt.next

	def sort(self):    # 插入排序，方式：交换两个节点
		p = self.head
		if p is None or p.next is None:
			return

		rem = p.next
		p.next = None
		while rem is not None:
			p = self.head
			q = None
			while p is not None and p.elem <= rem.elem:
				q = p
				p = p.next
			if q is None:
				self.head = rem
			else:
				q.next = rem
			q = rem
			rem = rem.next
			q.next = p




# l1 = LList()
# for i in range(10):
# 	l1.prepend(i)
# for i in range(11, 20):
# 	l1.append(i)
# l1.printall()
#
# # l1.for_each(print)
#
# # for i in l1.elements():
# # 	print(i)
#
# print("")
# # l1.insert(5, 111)
# # l1.printall()
# # print("")
# #
# # l1.delete(5)
# # l1.printall()
#
# print("")
# l1.reverse()
# l1.printall()
#
# print("")
# l1.sort1()
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
			p.next = self.head.next
			self.head.next = p

	def append(self, elem):
		self.prepend(elem)
		self.head = self.head.next

	def pop(self):
		if self.head is None:
			raise LinkedListUnderflow()
		elif self.head.next is None:
			self.head = None
		else:
			self.head.next = self.head.next.next

	def printall(self):
		if self.is_empty():
			return
		p = self.head.next
		while True:
			print(p.elem)
			if p is self.head:
				break
			p = p.next

# lc = LCist()
# for i in range(5):
# 	lc.prepend(i)
# 	lc.append(i)
# # lc.printall()
#
# lc.pop()
# lc.printall()


"""
	双链表
"""
# 双链表节点
class DLNode(LNode):
	def __init__(self, elem, prev=None, next=None):
		LNode.__init__(self, elem, next)
		self.prev = prev


class DLList(LList1):
	def __init__(self):
		LList1.__init__(self)

	def prepend(self, elem):
		p = DLNode(elem, None, self.head)
		if self.head is None:
			self.rear = p
		else:
			p.next.prev = p
		self.head = p

	def append(self, elem):
		p = DLNode(elem, self.rear, None)
		if self.head is None:
			self.head = p
		else:
			p.prev.next = p
		self.rear = p

	def pop(self):
		if self.head is None:
			raise LinkedListUnderflow()
		e = self.head.elem
		self.head = self.head.next
		if self.head is not None:
			self.head.prev = None
		return e

	def pop_last(self):
		if self.head is None:
			raise LinkedListUnderflow()
		e = self.rear.elem
		self.rear = self.rear.prev
		if self.rear is None:
			self.head = None
		else:
			self.rear.next = None
		return e

	def printall(self):
		p = self.head
		if self.head is None:
			return
		while p is not None:
			print(p.elem, end=" ")
			p = p.next


# dl = DLList()
# for i in range(5):
# 	dl.append(i)
# 	dl.prepend(i)
# dl.pop()
# dl.pop_last()
# dl.printall()



"""
	循环双链表
"""



"""
	josephus问题
	假设：n个人围坐一圈，现在从第k 个人开始报数，报到m 个人退出。
		 然后从下一个人开始继续报数，并按同样规则退出，直至所有人退出
"""
def josephus_A(n, k, m):   # 数组实现
	people = list(range(1, n+1))

	i = k-1
	for num in range(n):
		count = 0
		while count < m:
			if people[i] > 0:
				count += 1
			if count == m:
				print(people[i], end="")
				people[i] = 0
			i = (i+1) % n
		if num < n-1:
			print(", ", end=" ")
		else:
			print("")
	return

# josephus_A(10, 2, 7)


def josephus_L(n, k, m):
	people = list(range(1, n+1))

	num, i = n, k-1
	for num in range(n, 0, -1):
		i = (i + m-1) % num
		print(people.pop(i), end=", " if num > 1 else '\n')
	return


josephus_L(10, 2, 7)