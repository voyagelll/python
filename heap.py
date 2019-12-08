"""
    堆
    是一种经过排序的完全二叉树，其中任一非叶子节点的均值不大于（或不小于）其左孩子或右孩子节点的值

    最大堆：根节点的键值是所有堆节点键值中最大者
    最小堆：根节点的键值是所有堆节点键值中最小值
"""


class heap(object):
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) -1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        """
            先将元素放在最后，然后从后往前一次堆话
            这里已大顶堆为例，如果插入元素比父节点大，则交换，直到最后
        """
        self.data_list.append(data)
        index = len(self.data_list) -1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def removeMax(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2*index+1 <= total_index and self.data_list[2*index+1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index + 1
            if 2*index+2 <= total_index and self.data_list[2*index +2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index
