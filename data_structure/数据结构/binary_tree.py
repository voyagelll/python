"""
	二叉树
"""

class Node(object):
	def __init__(self, item):
		self.item = item 
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.item)


class Tree(object):
	def __init__(self):
		self.root = Node('root')

	def add(self, item):
		"""
			添加函数
		"""
		node = Node(item)
		# print(node)
		if self.root is None:
			self.root = node
		else:
			q = [self.root]
			while True:
				pop_node = q.pop(0)
				if pop_node.left is None:
					pop_node.left = node
					return
				elif pop_node.right is None:
					pop_node.right = node
					return 
				else:
					q.append(pop_node.left)
					q.append(pop_node.right)


	def get_parent(self, item):
		"""
			获取父节点
		"""
		if self.root.item == item:
			return None
		tmp = [self.root]
		while tmp:
			pop_node = tmp.pop(0)
			if pop_node.left and pop_node.left.item == item:
				return pop_node
			if pop_node.right and pop_node.right.item == item:
				return pop_node
			if pop_node.left is not None:
				tmp.append(pop_node.left)
			if pop_node.right is not None:
				tmp.append(pop_node.right)
		return None

	def delete(self, item):
		if self.root is None:
			return False

		parent = self.get_parent(item)
		if parent:
			del_node = parent.left if parent.left.item == item else parent.right
			if del_node.left is None:
				if parent.left.item == item:
					parent.left == del_node.right
				else:
					parent.right == del_node.right
				del del_node
				return True
			elif del_node.right is None:
				if parent.left.item == item:
					parent.left == del_node.left
				else:
					parent.right == del_node.left
				del del_node
				return True
			else:
				tmp_pre = del_node
				tmp_next = del_node.right
				if tmp_next.left is None:
					tmp_pre.right = tmp_next.right
					tmp_next.left = del_node.left
					tmp_next.right = del_node.right
				else:
					while tmp_next.left:
						tmp_pre = tmp_next
						tmp_next = tmp_next.left
					tmp_pre.left = tmp_next.right
					tmp_next.left = del_node.left
					tmp_next.right = del_node.right
				if parent.left.item == item:
					parent.left = tmp_next
				else:
					parent.right = tmp_next
				del del_node
				return True
		else:
			return False

	def inorder(self, node):
		"""
			中序遍历（左根右）
		"""
		if node is None:
			return []
		result = [node.item]
		left_item = self.inorder(node.left)
		right_item = self.inorder(node.right)
		return left_item + result + right_item

	def postorder(self, node):
		"""
			后序遍历（左右根）
		"""
		if node is None:
			return []
		result = [node.item]
		left_item = self.postorder(node.left)
		right_item = self.postorder(node.right)
		return left_item + right_item + result

	def preorder(self, node):
		"""
			先序遍历（根左右）
		"""
		if node is None:
			return []
		result = [node.item]
		left_item = self.preorder(node.left)
		right_item = self.preorder(node.right)
		return result + left_item + right_item


if __name__ == '__main__':
	items = [1,2,3,4,5,6,7,8,9,10]

	t = Tree()
	for item in items:
		t.add(item)

	print(t.get_parent(5))

	print(t.inorder(t.root))
	print(t.preorder(t.root))
	print(t.postorder(t.root))
