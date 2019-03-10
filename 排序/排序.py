# coding:utf-8

# 选择排序
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        newArr.append(arr.pop(smallest))
    return newArr

# --------------------
# 递归求最大值
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

# --------------------
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

# --------------------
# 冒泡排序
def bubbleSort(array):
    arr = array
    for i in range(1, len(arr)):
        flag = True
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                flag = False  
        if flag:
            break
    return arr

# --------------------
# 堆排序
def buildMaxHeap(arr):
    for i in range(int(len(arr)/2), -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1 
        heapify(arr, 0)
    return arr

# --------------------
# 计数排序
def countingSort(arr, maxValue):
    bucketLen = maxValue + 1
    bucket = [0]*bucketLen
    sortedIndex = 0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr

# --------------------
# 基数排序

print countingSort([5, 3, 6, 2, 10], 10)