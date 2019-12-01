from singe_link_list import Linked_List


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(Linked_List):
    # def __init__(self, head=None):
    #     self.head = head
    pass


if __name__ == '__main__':
    cll = SingleCycleLinkList()
    # print(help(cll))
    cll.init_list([1,2,3,4])
    cll.travel()