# coding:utf-8

def bucket_sort(array, n):
    # 1.创建n个空桶
    new_list = [[] for _ in range(n)]

    # 2.把arr[i] 插入到bucket[n*array[i]]
    for data in array:
        index = int(data * n)
        new_list[index].append(data)

    # 3.桶内排序
    for i in range(n):
        new_list[i].sort()

    # 4.产生新的排序后的列表
    index = 0
    for i in range(n):
        for j in range(len(new_list[i])):
            array[index] = new_list[i][j]
            index += 1
    return array


def main():
    array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    n = len(array)
    array = bucket_sort(array, n)
    print(array)


if __name__ == '__main__':
    main()