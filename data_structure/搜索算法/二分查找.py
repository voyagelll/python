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


seq = [1,2,3,4,5]
for i in [0,1,2,3,4,5,6]:
    print(jumpsearch(seq, i))



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

