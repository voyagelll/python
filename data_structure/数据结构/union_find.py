"""
    并查集：
    是一种数据结构，用于处理对 N 个元素的集合划分和判断是否属于同集合的问题。
    让每个元素构成一个单元素的集合，然后按一定顺序将属于同一组的元素所在的集合合并，其间，
    反复查找一个元素在哪个集合中。并查集是一种树型的数据结构，用于处理一些不相交集合的合并
    及查询问题
"""


class unionFind(object):
    def __init__(self, data_list):
        self.father_dict = {}
        self.size_dict = {}
        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        father = self.father_dict[node]
        if (node != father):    # 递归查找父节点
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        if node_a is None or node_b is None:
            return
        a_head = self.find(node_a)
        b_head = self.find(node_b)
        if (a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if (a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size


if __name__ == '__main__':
    a = [1,2,3,4,5]
    union_find = unionFind(a)
    union_find.union(1,2)
    union_find.union(3,5)
    union_find.union(3,1)
    print(union_find.is_same_set(2,5))
