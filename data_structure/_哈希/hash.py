# coding=gbk
"""
	��ϣ
		- �ǽ���һ���ȵ����룬ͨ��ɢ���㷨�任�ɹ̶����ȵ����
	
	��ϣ��
		- ���ݼ���ֵ���ʵ����ݽṹ
		  ͨ���Ѽ���ֵӳ�����һ��λ�������ʼ�¼���Լӿ�����ٶȣ�ӳ�亯����ɢ�к�������ż�¼�����ݣ�ɢ�б�
		- ����ʱ������ O(1)
		- �����ͻ
			* ����Ѱַ��
				H = (hash(k) + di) MOD m, i=1,2,3...k(k<=m-1)    [hash(k):ɢ�к�����di����������]
				1. ����̽����ɢ�У� di = 1,2,3...m-1
				2. ƽ��̽����ɢ�У� di = 1^2, -1^2, ...+-(k)^2 (k<=m/2)
				3. ���̽����ɢ�У� di = α�����
			* ��ɢ�з�
			* ����ַ��
			* �������������
			
	ժҪ�㷨
		- MD5
		- SHA

		- Ӧ��
			* �ļ�У��
			* ����ǰ��
"""

class hashtable1(object):
	def __init__(self):
		self.items = []

	def put(self, k, v):
		self.items.append((k, v))

	def get(self, k):
		for key, value in self.items:
			if (k==key):
				return value 


class hashtable2(object):
	# ֱ�Ӷ�ַ�����˷ѿռ�)
	def __init__(self):
		self.items = [None] * 100 

	def hash(self, a):
		return a*1+1 

	def put(self, k, v):
		self.items[self.hash(k)] = v 

	def get(self, k):
		hashcode = self.hash(k)
		return self.items[hashcode]


class hashtable3(object):
	# ���ŵ�ַ��������̽�⣩
	def __init__(self):
		self.capacity = 10 
		self.hash_table = [[None, None] for i in range(self.capacity)]
		self.num = 0 
		self.load_factor = 0.75

	def hash(self, k, i):
		h_value = (k+i) % self.capacity
		if self.hash_table[h_value][0] == k:
			return h_value 
		if self.hash_table[h_value][0] != None:
			i += 1 
			h_value = self.hash(k, i)
		return h_value 

	def resize(self):
		self.capacity = self.num * 2 
		temp = self.hash_table[:]
		self.hash_table = [[None, None] for i in range(self.capacity)]
		for i in temp:
			if (i[0] != None):
				hash_v = self.hash(i[0], 0)
				self.hash_table[hash_v][0] = i[0]
				self.hash_table[hash_v][1] = i[1]

	def put(self, k, v):
		hash_v = self.hash(k, 0)
		self.hash_table[hash_v][0] = k 
		self.hash_table[hash_v][1] = v 
		self.num = self.num + 1 
		if (self.num / len(self.hash_table) > self.load_factor):
			self.resize()

	def get(self, k):
		hash_v = self.hash(k, 0)
		return self.hash_table[hash_v]

table = hashtable3()
for i in range(1,13):
	table.put(i, i)
print(table.get(3))
print(table.hash_table)



"""
	�ж�����
		- �̳���
		- ɸѡ��
			1����n������ȫ���Ž����飬������Ϊ�϶�״̬
			2���������±���ż��������ȫ����Ϊ��״̬
			3��һ�α������鳤�ȵ�ƽ����������
			4�������ǰ���ִ��ڱ��϶�״̬�����䱳�������״̬��Ϊ��
"""

def find_prime(num):
	# �̳���1
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				print(num, 'is not prime num')
				print(i, '*', num//i, '=', num)
				break 
		else:
			print(num, 'is prime num')
	else:
		print(num, 'is not prime num')

# find_prime(7)


import math 

def prime_filter(num):
	# ɸѡ��
	primes_bool = [False, False] + [True]*(num-1)
	for i in range(3, len(primes_bool)):
		if i%2 == 0:
			primes_bool[i] = False 
	for i in range(3, int(math.sqrt(num))+1):
		if primes_bool[i] is True:
			for j in range(i+i, num+1, i):
				primes_bool[j] = False 
	primes = []
	for i, v in enumerate(primes_bool):
		if v is True:
			primes.append(i)
	return primes 


print(prime_filter(100))