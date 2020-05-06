"""
    二叉树实现
"""
class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = Node('root')

    def add(self, item):
        node = Node(item)
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
        if self.root.item == item:
            return None
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item:
                return pop_node.item
            if pop_node.right and pop_node.right.item == item:
                return pop_node.item
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
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left == del_node.left
                else:
                    parent.right = del_node.right
                del del_node
                return True
            else:
                tmp_pre = del_node
                # 待删除节点右子树
                tmp_next = del_node.right
                # 寻找将删除节点右子树中的最左子节点并完成替换
                if tmp_next.left is None:
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    tmp_pre.left = tmp_next.left
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


    def preorder(self, node):
        if node is None:
            return []
        res = [node.item]
        left_item = self.preorder(node.left)
        right_item = self.preorder(node.right)
        return res + left_item + right_item

    def inorder(self, node):
        if node is None:
            return []
        res = [node.item]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + res + right_item

    def postorder(self, node):
        if node is None:
            return []
        res = [node.item]
        left_item = self.postorder(node.left)
        right_item = self.postorder(node.right)
        return left_item + right_item + res


# if __name__ == '__main__':
#     t = Tree()
#     for i in range(10):
#         t.add(i)
#     print(t.preorder(t.root))
#     print(t.inorder(t.root))
#     print(t.postorder(t.root))
#
#     print(t.get_parent(0))
#     print(t.get_parent(4))



"""
    堆（优先队列）
"""
class heap():
    def __init__(self):
        self.data_list = []

    def insert(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def get_parent_index(self, index):
        if index == 0 or index>len(self.data_list)-1:
            return None
        else:
            return (index-1)>>1

    def removeMax(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2*index+1 < total_index and self.data_list[2*index+1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index+1
            if 2*index+2 < total_index and self.data_list[2*index+2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index+2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index



h = heap()
for i in range(5):
    h.insert(i)
print(h.data_list)
print(h.removeMax())
print(h.data_list)
h.insert(5)
h.insert(5)
print(h.data_list)
print(h.removeMax())
print(h.data_list)



