"""
    - 树
        * 是一种非常高效的非线性存储结构。
        * 二叉树： 每个节点都至多有两个子节点的树
        * 满二叉树： 每层节点数都是最大节点数
        * 完全二叉树：就是叶子节点都在最底下两层，最后一层叶子节点靠左排列
                      且出了最后一层，其他层的节点个数都要达到最大

        * 二叉搜索树（二叉排序树）
            1、若左子树不为空，则左子树上所有节点的值小于它的根节点的值
            2、若右子树不为空，则右子树上所有节点的值大于它的根节点的值
            3、左，右子树也分别为二叉搜索树

        * 平衡二叉树（AVL树）：自平衡二叉搜索树
            1、是一棵二叉搜索树
            2、左右子节点也是AVL树
            3、拥有二叉搜索树的基本特点
            4、每个节点的左右子节点的高度之差的绝对值不超过1

        * 红黑树
            - 性质
                1、节点是红色或者黑色
                2、根是黑色
                3、所有叶子都是黑色
                4、每个红色节点必须有两个黑色的子节点
                5、从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点
            - 上述性质确保了：红黑树从根到叶子的最长的可能路径不多于最短的可能路径的两倍长
            - 相对于AVl 树，红黑树牺牲了部分平衡性以换取插入\删除时少量的旋转操作

        * B 树
            1、所有键值分布在整棵树中
            2、搜索有可能在非叶子节点结束，在关键字全集内做以此查找，性能逼近二分查找
            3、每个节点最多拥有m个子树，根节点至少有2个子树。
            4、分支节点至少拥有m/2颗子树
            5、所有叶子节点都在同一层，每个节点最多可以有 m-1 个key，并且以升序排列

        * B+ 树
            1、每个节点可以包含更多的节点，1.为了降低树的高度，2、将数据范围变为多个区间，区间越多，数据检索跃快
            2、非叶子节点存储key， 叶子节点存储key 和数据
            3、叶子节点两两指针符合磁盘的预读特性，顺序查询性能更高


    - 堆（优先队列）
        * 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值

        * 最大堆：根节点的键值是所有堆节点键值中最大的
        * 最小堆：根节点的键值是所有堆节点键值中最小的
"""

"""
    二叉树实现
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
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del_node
                return True
            else:
                tmp_pre = del_node
                # 待删除节点右子树
                tmp_next = del_node.right
                # 寻找待删除节点右子树中的最左子节点并完成替代
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
                # 如果待删除节点是父亲节点的左孩子
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

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

    def preorder(self, node):
        if node is None:
            return []
        res = [node.item]
        left_item = self.preorder(node.left)
        right_item = self.preorder(node.right)
        return res + left_item + right_item


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    print(tree.inorder(tree.root))
    print(tree.preorder(tree.root))
    print(tree.postorder(tree.root))
    print(tree.get_parent(6))
    tree.delete(0)
    tree.delete(1)
    print(tree.inorder(tree.root))
