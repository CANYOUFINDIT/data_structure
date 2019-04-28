# coding:utf-8

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

print bubbleSort([7, 8, 4, 5, 6, 2, 9, 1, 3, 0])