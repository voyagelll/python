# coding=gbk

"""
	# �ѣ����ȶ��У�
	- ��һ�־����������ȫ��������������һ��Ҷ�ӽڵ��ֵ�������ڣ���С�ڣ������Ӻ��Һ��ӽڵ��ֵ
	- ���ѣ����ڵ�ļ�ֵ�����жѽڵ��ֵ�������
	- ��С�ѣ����ڵ�ļ�ֵ�����жѽڵ��ֵ�е���С��
"""


class heap(object):
	def __init__(self):
		self.data_list = []

	def get_parent_index(self, index):
		if index == 0 or index > len(self.data_list)-1:
			return None 
		else:
			return (index-1) >> 1 

	def swap(self, index_a, index_b):
		self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

	def insert(self, data):
		# �Ƚ�Ԫ�ط������Ȼ��Ӻ���ǰ���ζѻ�
		self.data_list.append(data)
		index = len(self.data_list) - 1
		parent = self.get_parent_index(index) 
		# ��������Ԫ�رȸ��ڵ���򽻻���֪�����
		while parent is not None and self.data_list[parent] < self.data_list[index]:
			self.swap(parent, index)
			index = parnet 
			parent = self.get_parent_index(parent)

	def removeMax(self):
		# ɾ���Ѷ�Ԫ�أ�Ȼ�����һ��Ԫ�ط��ڶѶ����ٴ����������ζѻ�
		remove_data = self.data_list[0]
		self.data_list[0] = self.data_list[-1]
		del self.data_list[-1]
		# �ѻ�
		self.heapify(0)
		return remove_data

	def heapify(self, index):
		total_index = len(self.data_list) - 1 
		while True:
			maxvalue_index = index 
			if 2*index + 1 <= total_index and self.data_list[2*index+1] > self.data_list[maxvalue_index]:
				maxvalue_index = 2*index + 2 
			if 2*index + 2 <= total_index and self.data_list[2*index+2] > self.data_list[maxvalue_index]:
				maxvalue_index = 2*index+2
			if maxvalue_index == index:
				break 
			self.swap(index, maxvalue_index)
			index = maxvalue_index 


# class heap(object):
#     def __init__(self):
#         # ��ʼ��һ���նѣ�ʹ���������ڴ�Ŷ�Ԫ�أ���ʡ�洢
#         self.data_list = []

#     def get_parent_index(self,index):
#         if index == 0 or index > len(self.data_list) -1:
#             return None
#         # ���ظ��ڵ���±�
#         else:
#             # >> �����ƶ������
#             # �� >> ��ߵ�����������λȫ���ƶ�
#             # ����2 >> 1 �Ľ��Ϊ 1
#             # �ò�������Ϊ 0000 0010 �����Ϊ 0000 0001
#             return (index -1) >> 1

#     def swap(self,index_a,index_b):
#         # ���������е�����Ԫ��
#         self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

#     def insert(self, data):
#         # �Ȱ�Ԫ�ط������Ȼ��Ӻ���ǰ���ζѻ�
#         # �����Դ󶥶�Ϊ�����������Ԫ�رȸ��ڵ���򽻻���ֱ�����
#         self.data_list.append(data)
#         index = len(self.data_list) - 1
#         parent = self.get_parent_index(index)
#         # ѭ����ֱ����Ԫ�س�Ϊ�Ѷ�����С�ڸ��ڵ㣨���ڴ󶥶�)
#         while parent is not None and self.data_list[parent] < self.data_list[index]:
#             # ��������
#             self.swap(parent, index)
#             index = parent
#             parent = self.get_parent_index(parent)

#     def removeMax(self):
#         # ɾ���Ѷ�Ԫ�أ�Ȼ�����һ��Ԫ�ط��ڶѶ����ٴ����������ζѻ�
#         remove_data = self.data_list[0]
#         self.data_list[0] = self.data_list[-1]
#         del self.data_list[-1]

#         # �ѻ�
#         self.heapify(0)
#         print(self.data_list)
#         return remove_data

#     def heapify(self,index):
#         # �������¶ѻ����� index ��ʼ�ѻ����� (�󶥶�)
#         total_index = len(self.data_list) -1
#         while True:
#             maxvalue_index = index
#             if 2*index +1 <=  total_index and self.data_list[2*index +1] > self.data_list[maxvalue_index]:
#                 maxvalue_index = 2*index +1
#             if 2*index +2 <=  total_index and self.data_list[2*index +2] > self.data_list[maxvalue_index]:
#                 maxvalue_index = 2*index +2
#             if maxvalue_index == index:
#                 break
#             self.swap(index,maxvalue_index)
#             index = maxvalue_index

h = heap()
h.insert(10)
h.insert(9)
h.insert(6)
h.insert(7)
h.insert(8)
h.insert(2)
h.insert(5)
h.insert(1)
h.insert(4)
h.insert(3)
print(h.data_list)
print([h.removeMax() for _ in range(5)])
