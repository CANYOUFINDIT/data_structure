# coding:utf-8
'''
给定一个正整数，实现一个方法来求出离该整数最近的大于自身的“换位数”。
换位数：就是把一个整数各个数位的数字进行全排列，从而得到新的整数。例如53241和23541。

获得最近换位数的三个步骤：

1.从后向前查看逆序区域，找到逆序区域的前一位，也就是数字置换的边界

2.把逆序区域的前一位和逆序区域中刚刚大于它的数字交换位置

3.把原来的逆序区域转为顺序
'''

# 主流程，返回最近一个大于自身的相同数字组成的整数。
def findNearestNumber(number_list):
    numbersCopy = number_list
    if numbersCopy is None:
        return None
    # 1.从后向前查看逆序区域，找到逆序区域的前一位，也就是数字置换的边界
    index = findTransferPoint(numbersCopy)
    # 如果数字置换边界是0，说明整个数组已经逆序，无法得到更大的相同数字组成的整数，返回自身
    if index == 0:
        return None
    # 2.把逆序区域的前一位和逆序区域中刚刚大于它的数字交换位置
    exchangeHead(numbersCopy, index)
    # 3.把原来的逆序区域转为顺序
    reverse(numbersCopy, index)
    return numbersCopy


# 获取逆序区域的边界
def findTransferPoint(number_list):
    # reversed生成一份倒序列表的拷贝
    for i in reversed(range(0, len(number_list))):
        if number_list[i] > number_list[i-1]:
            return i
    return 0


# 将逆序区域的前一位与逆序区域中大于它的最小值换位
def exchangeHead(number_list, index):
    head = number_list[index-1]
    for i in reversed(range(0, len(number_list))):
        if head < number_list[i]:
            number_list[index-1] = number_list[i]
            number_list[i] = head
            break
    return number_list


# 将替换后的逆序区域转为顺序
def reverse(number_list, index):
    i = index
    j = len(number_list)
    for i, j in zip(range(index, len(number_list)), reversed(range(0, len(number_list)))):
        temp = number_list[i]
        number_list[i] = number_list[j]
        number_list[j] = temp
    return num_list

if __name__ == "__main__":
    num_list = [5, 4, 3, 1, 2]
    # 获取10个换位数
    for i in range(0, 10):
        num_list = findNearestNumber(num_list)
        print num_list