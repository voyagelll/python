"""
    链表
    - 是物理存储单元上非连续的、非顺序的存储结构，数据元素的逻辑顺序是通过链表的指定地址实现。
      每个元素包含两个节点，一个是数据域，另一个是指针域。
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        new_element = Node(new_element)
        current = self.head
        # print(current)
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def is_empty(self):
        return not self.head

    def insert(self, position, new_element):
        new_element = Node(new_element)
        if position < 0 or position > self.get_length():
            raise IndexError('Insert key out of range')
        temp = self.head
        if position == 0:
            new_element.next = temp
            self.head = new_element
            return
        i = 0
        while i < position:
            pre = temp
            temp = temp.next
            i += 1
        pre.next = new_element
        new_element.next = temp

    def remove(self, position):
        if position < 0 or position > self.get_length()-1:
            raise IndexError('Index out of range')
        i = 0
        temp = self.head
        while temp is not None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return
            pre = temp
            temp = temp.next
            i += 1
            if i == position:
                pre.next = temp.next
                temp.next = None
                return

    def get_length(self):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        return length

    # 遍历
    def travel(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    # 将链表逆序
    def reverse(self):
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre

    # 将列表转为链表
    def initlist(self, data_list):
        self.head = Node(data_list[0])
        temp = self.head
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    # 交换两个元素的位置
    def switch(self, item1, item2):
        pass



ls = Linked_list()
ls.append(1)
ls.append(2)
ls.append(3)
ls.append(1)
print(ls.get_length())
ls.insert(3,5)
print(ls.get_length())
ls.travel()
print("")
ls.remove(2)
ls.remove(0)
ls.travel()

ls.reverse()
print("")
ls.travel()

print("")
ls.initlist([3,2,1,0])
ls.travel()

print("")

