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
		node = Node(elem)
		if self.is_empty():
			self.head = node
			self.rear = node
		else:
			self.rear.next = node
			self.rear = node

	def dequeue(self):
		if self.is_empty():
			return 
		else:
			val = self.head.elem
			self.head = self.head.next
			return val

	def peek(self):
		if self.is_empty():
			return 
		else:
			return self.head.elem

	def travel(self):
		cur = self.head
		while cur:
			print(cur.elem, end=" ")
			cur = cur.next
		print("")



"""
	队列列表实现
"""


if __name__ == '__main__':
	q = Queue()
	print(q.is_empty())
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.travel()

	print(q.dequeue())
	q.travel()
	print(q.dequeue())
	q.travel()

	print(q.peek())