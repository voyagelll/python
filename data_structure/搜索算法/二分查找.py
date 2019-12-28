"""
    二分搜索
"""
def binary_search(seq, tar):
    l = 0
    r = len(seq)
    while l <= r:
        mid = (l + r) // 2
        cur_item = seq[mid]
        if cur_item == tar:
            return mid, cur_item
        elif tar < cur_item:
            r = mid - 1
        else:
            l = mid + 1
    return None


# seq = [1,2,3,4,5]
# for i in [0,1,2,3,4,5,6]:
#     print(binary_search(seq, i))


"""
    插值搜索
    * 适用性
        表长，关键字分布较均匀的表，差值搜索比二分搜索要好
    * 基本思想
        基于二分搜索，只是在取中点的时候把比例参数 1/2 修改为自适应
    * 复杂度
        最坏时间复杂度：O(logn)
        最好时间复杂度：O(1)
        平均时间复杂度：O(loglogn)        
"""
def insert_search(sorted_sequence, tar):
    l = 0
    r = len(sorted_sequence) - 1
    while l < r:
        mid = l + ((tar - sorted_sequence[l]) * (r - l)) // \
              (sorted_sequence[r] - sorted_sequence[l])
        if mid < 0 or mid >= len(sorted_sequence):
            return None
        cur_item = sorted_sequence[mid]
        if cur_item == tar:
            return mid
        elif tar < cur_item:
            r = mid - 1
        else:
            l = mid + 1
    return None


# seq = [1,2,3,4,5]
# for i in [0,1,2,3,4,5,6]:
#     print(insert_search(seq, i))



"""
    跳跃搜索
    * 基本思想
        基于二分搜索算法，采用固定间隔进行跳跃，知道找到一个复核目标元素的区间，
        然后在该区间使用现行搜索
    * 复杂度
        最坏时间复杂度：O(n*(1/2))
        最好时间复杂度：O(n*(1/2))
        平均时间复杂度：O(n*(1/2))
"""
import math


def jumpsearch(seq, tar):
    n = len(seq)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while seq[min(step, n)-1] < tar:
        prev = step
        step = step + int(math.floor(math.sqrt(n)))
        if prev >= n:
            return None
    while seq[prev] < tar:
        prev += 1
        if prev == min(step, n):
            return None
    if seq[prev] == tar:
        return prev
    else:
        return None


# seq = [1,2,3,4,5]
# for i in [0,1,2,3,4,5,6]:
#     print(jumpsearch(seq, i))



"""
    快速搜索
    * 适用性
        用于查找无序列表中的第 k 个最小元素或最大元素
    * 基于思想
        二分搜索算法，采用固定间隔进行跳跃，直到找到一个符合目标元素的区间，然后在该区间使用现行搜索
    * 复杂度
        最坏时间复杂度：O(n^2)
        最好时间复杂度：O(n)
        平均时间复杂度：O(n)
"""
import random


def partition(sequence, left, right, pivot_index):
    pivot_value = sequence[pivot_index]
    sequence[pivot_index], sequence[right] = sequence[right], sequence[pivot_index]
    store_index = left
    for i in range(left, right):
        if sequence[i] < pivot_value:
            sequence[store_index], sequence[i] = sequence[i], sequence[store_index]
            store_index = store_index + 1
    sequence[store_index], sequence[right] = sequence[right], sequence[store_index]
    return store_index



"""
    哈希搜索
    * 适用性
        一个简单无需数组可实现索引关系
    * 基本思想
        如果所有的键都是整数，就可以使用一个简单的无序数组来实现。
        将键作为索引，值为其对应的值
    * 复杂度
        最坏时间复杂度：O(1)
        最好时间复杂度：O(1)
        平均时间复杂度：O(1)
"""

class HashTable:
    def __init__(self, size):
        self.elem = [None for i in range(size)]
        self.count = size

    def hash(self, key):
        return key % self.count

    def insert_hash(self, key):
        address = self.hash(key)
        while self.elem[address]:
            address = (address+1) % self.count
        self.elem[address] = key

    def search_hash(self, key):
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star:
                return False
        return True, address


list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
hash_table = HashTable(12)
for i in list_a:
    hash_table.insert_hash(i)
for i in hash_table.elem:
    if i:
        print((i, hash_table.elem.index(i)), end=" ")
print("\n")
print(hash_table.search_hash(15))
print(hash_table.search_hash(33))


