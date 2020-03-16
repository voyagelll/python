# 空栈弹出异常类
class StackUnderflow(ValueError):
	pass 



# 栈的列表实现
class SStack():
	def __init__(self):
		self.elem = []

	def is_empty(self):
		return self.elem == []

	def top(self):
		if self.elem == []:
			raise StackUnderflow()
		return self.elem[-1]

	def push(self, elem):
		self.elem.append(elem)

	def pop(self):
		if self.elem == []:
			raise StackUnderflow()
		return self.elem.pop()


# s = SStack()
# s.push(1)
# s.push(2)
# s.push(3)
# while not s.is_empty():
# 	print(s.pop())



# 栈的链表实现
from chaper_3__线性表 import LNode

class LStack():
	def __init__(self):
		self.top  = None 

	def is_empty(self):
		return self.top is None

	def top(self):
		if self.top is None:
			raise StackUnderflow()
		return self.top.elem 

	def push(self, elem):
		self.top = LNode(elem, self.top)

	def pop(self):
		if self.top is None:
			raise StackUnderflow()
		e = self.top.elem 
		self.top = self.top.next 
		return e 


# ls = LStack()
# ls.push(1)
# ls.push(2)
# ls.push(3)
# while not ls.is_empty():
# 	print(ls.pop())



"""
	栈的应用：
	* 括号匹配
"""
# 括号匹配
def check_parens(text):
	parens = "{}[]()"
	open_parens = "{[("
	opposite = {"}":"{", "]":"[", ")":"("}

	def parentheses(text):
		i, text_len = 0, len(text)
		while True:
			while i<text_len and text[i] not in parens:
				i += 1 
			if i >= text_len:
				return 
			yield text[i], i 
			i += 1

	st = SStack()

	for pr, i in parentheses(text):
		if pr in open_parens:
			st.push(pr)
		elif st.pop() != opposite[pr]:
			print("unmatch is found at ", i, "for ", pr)
			return False
	print("All paratheses are matched")
	return True

check_parens("{}]")