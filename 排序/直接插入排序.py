def insertSort(arr):
    for i in range(len(arr)-1):
        temp = arr[i+1]
        j = i
        while j > -1 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

print insertSort([7, 8, 4, 5, 6, 2, 9, 1, 3, 0])