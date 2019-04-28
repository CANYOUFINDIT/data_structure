def selectSort(arr):
    new_arr = []
    for i in range(len(arr)):
        temp = arr[0]
        smallest = 0
        for i in range(1, len(arr)):
            if arr[i] < temp:
                temp = arr[i]
                smallest = i
        new_arr.append(arr.pop(smallest))
    return new_arr

print selectSort([7, 8, 4, 5, 6, 2, 9, 1, 3, 0])