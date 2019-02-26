# coding:utf-8

# 二分查找,时间复杂度O(logn)
def binary_search(list, item):
    # low和high用于跟踪要在其中查找的列表部分
    low = 0
    high = len(list) - 1
    # 只要范围没有缩小到只包含一个元素
    while low <= high:
        # 如果(low + high)不是偶数，Python自动将mid向下圆整。
        mid = (low + high)/2
        guess = list[mid]
        # 找到了元素
        if guess == item:
            return mid
        # 猜的数字大了
        if guess > item:
            high = mid - 1
        # 猜的数字小了
        else:
            low = mid + 1
    # 没有指定元素
    return None

my_list = range(1, 100)
print binary_search(my_list, 55)