# coding:utf-8

def buildMaxHeap(arr):
    # 遍历所有非叶节点
    for i in range(int(len(arr)/2), -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    # 非叶结点arr[i]的左右结点下标
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    # 如果子结点比该非叶结点大，则将二者换位
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    # 换位
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    # 全局变量，保存原数组的长度
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1 
        heapify(arr, 0)
    return arr

print heapSort([7, 8, 4, 5, 6, 2, 9, 1, 3, 0])