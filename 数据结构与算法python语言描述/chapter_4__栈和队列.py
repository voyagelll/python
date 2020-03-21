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
	print([i for i in parentheses(text)])
	st = SStack()

	for pr, i in parentheses(text):
		print(pr, i)
		if pr in open_parens:
			st.push(pr)
		elif st.pop() != opposite[pr]:
			print("unmatch is found at ", i, "for ", pr)
			return False
	print("All paratheses are matched")
	return True

# check_parens("{})aa")


"""
	后缀表达式
"""

# 增加一个求栈深度的方法
class ESStack(SStack):
	def depth(self):
		return len(self.elem)


def suf_exp_evaluator(exp):
	operators = '+-*/'
	st = ESStack()

	for x in exp:
		if x not in operators:
			st.push(float(x))
			continue
		if st.depth() < 2:
			raise SyntaxError('Short of operand(s)')
		a = st.pop()
		b = st.pop()

		if x == '+':
			c = a+b 
		elif x == '-':
			c = b-a
		elif x == '*':
			c = a*b
		elif x=='/':
			c = b/a 
		else:
			break 
		st.push(c)
	if st.depth() == 1:
		return st.pop()
	raise SyntaxError('Extra operand(s)')


print(suf_exp_evaluator('3 5 - 6 17 4 * + * 3 /'.split(' ')))



"""
	背包问题
"""






"""
	队列
"""

# 队列异常
class QueueUnderflow(ValueError):
	pass 


class SQueue():
	def __init__(self, init_len=8):
		self._len = init_len 
		self._elems = [0]*init_len 
		self._head = 0 
		self._num = 0 

	def is_empty(self):
		return self._num == 0 

	def peek(self):
		if self._num == 0:
			raise QueueUnderflow()
		return self._elems[self._head]

	def dequeue(self):
		if self._num == 0:
			raise QueueUnderflow()
		e = self._elems(self._head)
		self._head = (self._head+1) % self._len 
		self.num -= 1 
		return e 

	def enqueue(self, e):
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head+self._num) % self._len] = e 
		self._num += 1 

	def __extend(self):
		old_len = self._len 
		self._len *= 2 
		new_elems = [0]*self._len 
		for i in range(old_len):
			new_elems[i] = self._elems[(self._head+i)%old_len]
		self._elems, self_head = new_elems, 0 

		


"""
	栈和队列的应用
"""

# 迷宫求解
dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def mark(maze, pos):            # 已经到过的位置
	maze[pos[0]][pos[1]] = 2

def passable(maze, pos):        # 检查位置是否可行
	return maze[pos[0]][pos[1]] == 0

# 递归实现
def find_path(maze, pos, end):
	mark(maze, pos)
	if pos == end:
		print(pos, ned=" ")
		return True 
	for i in range(4):
		nextp = pos[0]+dirs[i][0], pos[1]+dirs[i][1]
		if passable(maze, nextp):
			if find_path(maze, nextp, end):
				print(pos, end=" ")
				return True 
	return False 



# 回溯法（栈）
def maze_solver(maze, start, end):
	if start == end:
		print(start)
		return 
	st = SStack()
	mark(maze, start)
	st.push((start, 0))
	while not st.i_empty():
		pos, nxt = st.pop()
		for i in range(nxt, 4):
			nextp = (pos[0] + dirs[i][0],
					 pos[1] + dirs[i][1])
		if nextp == end:
			print_path(end, pos, st)
			return 
		if passable(maze, nextp):
			st.push((pos, i+1))
			mark(maze, nextp)
			st.push((nextp, 0))
			break 
	print("No path, found")
	
