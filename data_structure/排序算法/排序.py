
"""
	冒泡排序
	* 算法原理
		比较相邻的元素，如果第一个比第二大，就交换它们。
		从1，n-1个元素开始，依次遍历
	* 复杂度
		最坏时间复杂度：O(n^2)
		最好时间复杂度：O(n)
		平均时间复杂度：O(n^2)		
"""
def bubble_sort(sequence):
	for i in range(1, len(sequence)):
		for j in range(0, len(sequence)-i):
			if sequence[j] > sequence[j+1]:
				sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
	return sequence 


l = [8,8,7,5,4,2,2,1,1,1,0,6,9,9]
# print(bubble_sort(l))


def bubble(l):
	for i in range(1, len(l)):
		for j in range(0, len(l)-i):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
	return l

# print(bubble(l))

def bubble(l):
	for i in range(1, len(l)):
		for j in range(0, len(l)-i):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
	return l

print('bubble:', bubble(l))


"""
	选择排序
	* 算法原理
		1、首先在为排序的序列中找到最大（小）元素，存放到排序序列的起始位置。
		2、再从剩余未排序元素中继续寻找最小（大）㢝，然后放到已排序序列的末尾
		3、重复第二步，直到所有元素均排序完成
	* 复杂度
		最坏时间复杂度：O(n^2)
		最好时间复杂度：O(n^2)
		平均时间复杂度：O(n^2)
"""
def select_sort(sequence):
	for i in range(len(sequence)-1):
		minIndex = i 
		for j in range(i+1, len(sequence)):
			if sequence[j] < sequence[minIndex]:
				minIndex = j 
		sequence[i], sequence[minIndex] = sequence[minIndex], sequence[i]
	return sequence

# print(select_sort(l))


def select(l):
	for i in range(len(l)):
		minIndex = i
		for j in range(i+1, len(l)):
			if l[minIndex] > l[j]:
				minIndex = j
		l[minIndex], l[i] = l[i], l[minIndex]
	return l

# print(select(l))


def select_(l):
	for i in range(len(l)):
		mi = 0
		for j in range(i, len(l)):
			if l[i] > l[j]:
				mi = j
		l[mi], l[j] = l[j], l[mi]
	return l

print('select:', select_(l))


"""
	插入排序
	* 算法原理
		1、从第一个元素开始，该元素可以认为已经被排序
		2、取出下一个元素，在已经排序的元素序列中从后向前扫描
		3、如果该元素（已排序)大于新元素，将该元素移到下一位置
		4、重复步骤3，知道找到已排序的元素小于或者等于新元素的位置
		5、将新元素插入到该位置后
		6、重复步骤2-5
	* 复杂度
		最坏时间复杂度：O(n^2)
		最好时间复杂度：O(n^2)
		平均时间复杂度：O(n^2)
"""
def insert_sort(sequence):
	for index in range(1, len(sequence)):
		while (index>0 and sequence[index-1]>sequence[index]):
			sequence[index], sequence[index-1] = sequence[index-1], sequence[index]
			index = index - 1 
	return sequence 

# print(insert_sort(l))


def insert(l):
	for i in range(1, len(l)):
		while i>0 and l[i-1]>l[i]:
			l[i], l[i-1] = l[i-1], l[i]
			i -= 1
	return l

# print(insert(l))

def insert_(l):
	for i in range(1, len(l)):
		while i>0 and l[i-1]>l[i]:
			l[i], l[i-1] = l[i-1], l[i]
			i -= 1
	return l

print('insert:', insert_(l))


"""
	希尔排序
	* 算法原理
		先将整个带排序的记录序列分割为若干子序列分别进行直接插入排序，待整个序列中的记录基本有序时，
		再对全体记录进行插入排序
	* 复杂度
		最坏时间复杂度：O(n(logn)^2)
		最好时间复杂度：O(nlogn)
		平均时间复杂度：取决于间隔序列		
"""
def shell_sort(sequence):
	gap = len(sequence)
	while gap > 1:
		gap = gap // 2 
		for i in range(gap, len(sequence)):
			for j in range(i%gap, i, gap):
				# print(i%gap, i, gap, list(range(i%gap, i, gap)))
				if sequence[i] < sequence[j]:
					sequence[i], sequence[j] = sequence[j], sequence[i]
	return sequence 


# print(shell_sort(l))


def shell(l):
	gap = len(l)
	while gap > 1:
		gap = gap//2
		for i in range(gap, len(l)):
			print(i%gap, i, gap, list(range(i%gap, i, gap)))
			for j in range(i%gap, i, gap):
				if l[i] < l[j]:
					l[i], l[j] = l[j], l[i]
	return l

# print(shell(l))


"""
	归并排序
	* 算法原理
		1、把长度为n 的输入序列分为两个长度为 n/2 的子序列
		2、对这两个子序列分别采用归并排序
		3、将两个排序好的子序列合并成一个最终的排序序列
	* 复杂度
		最坏时间复杂度：O(nlogn)
		最好时间复杂度：O(nlogn)
		平均时间复杂度：O(nlogn)
"""
import math 

def merge_sort(sequence):
	if (len(sequence)<2):
		return sequence 
	mid = math.floor(len(sequence)/2)
	left, right = sequence[0:mid], sequence[mid:]
	return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
	result = []
	while left and right:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result  


# print(merge_sort(l))


def merge_sort_(l):
	if len(l) < 2:
		return l
	mid = math.floor(len(l)/2)
	left, right = l[0:mid], l[mid:]
	return merge_(merge_sort_(left), merge_sort_(right))

def merge_(left, right):
	result = []
	while left and right:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result

# print(merge_sort_(l))


"""
	快速排序
	* 算法思想：
		1、从数列中跳出一个元素，成为基准
		2、重新排序数列，所有元素比基准小的放在基准前面，比基准大的移动到基准后面
		3、递归把小于基准和大于基准的子数列排序
	* 复杂度
		最坏时间复杂度：O(n^2)
		最好时间复杂度：O(n - nlogn)
		平均时间复杂度：O(nlogn)
"""
def quick_sort(l):
	def recursive(first, last):
		if first >= last:
			return l 
		low = first
		high = last 
		mid = l[low]

		while low<high:
			while low<high and l[high]>=mid:
				high -= 1 
			l[low] = l[high]
			while low<high and l[low]<mid:
				low += 1 
			l[high] = l[low]
		l[low] = mid 
		recursive(0, low-1)
		recursive(low+1, last)
	recursive(0, len(l)-1)
	return l

# print(quick_sort(l))
# print(l)


def quick(l):
	def recursive(first, last):
		if first >= last:
			return l
		high = last
		low = first
		mid = l[low]

		while low<high:
			while low<high and l[high]>=mid:
				high -= 1
			l[low] = l[high]
			while low<high and l[low]<=mid:
				low += 1
			l[high] = l[low]
		l[low] = mid
		recursive(0, low-1)
		recursive(low+1, last)
	recursive(0, len(l)-1)
	return l

print('quick:', quick(l))



"""
	堆排序
	* 算法原理
		1、将初始待排序关键字序列构建成大顶堆
		2、将堆顶元素R[1]与最后一个元素R[n]交换,
		  此时得到新的无序区（R[1]...R[n-1])和新的有序区R[n]且满足R【1..n-1] < R[n]
		3、由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区R[1]...R[n-1]
		  调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区（R【1】...R[n-1])
		  和新的有序区（R[n-1],R[n])。不断重复次过程知道有序去元素个数为 n-1
	* 复杂度
		最坏时间复杂度：O(nlogn)
		最好时间复杂度：O(nlogn)
		平均时间复杂度：O(nlogn)
"""
import random 

def heap_sort(sequence):
	def heap_adjust(parent):
		child = 2*parent + 1 
		while child < len(heap):
			if child+1 < len(heap):
				if heap[child+1] > heap[child]:
					child = child + 1 
			if heap[parent] >= heap[child]:
				break 
			heap[parent], heap[child] = heap[child], heap[parent]
			parent, child = child, 2*child+1 

	heap, sequence = sequence.copy(), []
	for i in range(len(heap)//2, -1, -1):
		heap_adjust(i)
	while len(heap) != 0:
		heap[0], heap[-1] = heap[-1], heap[0]
		sequence.insert(0, heap.pop())
		heap_adjust(0)
	return sequence 


# print(heap_sort(l))


"""
	计数排序
	* 算法原理
		1、找出待排序数组中最大和最小的元素
		2、统计数组中每个值为i的元素出现的次数，存入数组C的第i项
		3、对所有的计数累加（从C中的第一个元素开始，每一项和前一项想加）
		4、反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
	* 复杂度分析
		最坏时间复杂度：O(n+k)
		最好时间复杂度：O(n+k)
		平均时间复杂度：O(n+k)
"""
def countingSort(arr, maxValue):
	bucketLen = maxValue + 1
	bucket = [0] * bucketLen
	sortedIndex = 0
	arrLen = len(arr)
	for i in range(arrLen):
		if not bucket[arr[i]]:
			bucket[arr[i]] = 0
		bucket[arr[i]] += 1
	for j in range(bucketLen):
		while bucket[j]>0:
			arr[sortedIndex] = j
			sortedIndex += 1
			bucket[j] -= 1
	return arr

# print(countingSort(l, max(l)))



"""
	桶排序
	* 算法原理
		桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键在于映射函数的确定
	* 复杂度分析
		最坏时间复杂度：O(n+k)
		最好时间复杂度：O(n)
		平均时间复杂度：O(n)
"""
def insertion_sort(sequence):
	for index in range(1, len(sequence)):
		while (index>0 and sequence[index-1] > sequence[index]):
			sequence[index], sequence[index-1] = sequence[index-1], sequence[index]
			index = index - 1
	return sequence


DEFAULT_BUCKET_SIZE = 5


def bucket_sort(sequence, bucketSize=DEFAULT_BUCKET_SIZE):
	print(sequence)
	if (len(sequence)==0):
		return []
	maxValue = sequence[0]
	minValue = sequence[0]
	for i in range(0, len(sequence)):
		if sequence[i] < minValue:
			minValue = sequence[i]
		elif sequence[i] > maxValue:
			maxValue = sequence[i]
	bucketCount = math.floor((maxValue-minValue) / bucketSize) + 1
	buckets = []
	for i in range(0, bucketCount):
		buckets.append([])
	for i in range(0, len(sequence)):
		buckets[math.floor((sequence[i] - minValue) / bucketSize)].append(sequence[i])
	sortedArray = []
	print(buckets)
	for i in range(0, len(buckets)):
		insertion_sort(buckets[i])
		for j in range(0, len(buckets[i])):
			sortedArray.append(buckets[i][j])
	return sortedArray

# print(bucket_sort(l))










