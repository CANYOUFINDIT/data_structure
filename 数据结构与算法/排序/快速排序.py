# coding:utf-8

# 快速排序
def quicksort(array):
    if len(array) < 2:
        # 基线条件：为空或只包含一个元素的数组是“有序”的
        return array
    else:
        # 递归条件
        pivot = array[0]
        # 由所有小于基准线的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准线的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([7, 8, 4, 5, 6, 2, 9, 1, 3, 0])