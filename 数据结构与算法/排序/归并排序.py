# coding:utf-8

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = int(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

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

print mergeSort([7, 8, 4, 5, 6, 2, 9, 1, 3, 0])