# coding:utf-8
'''
一个人爬楼梯，每次只能爬1个或2个台阶，假设有n个台阶，那么这个人有多少种不同的爬楼梯方法？
'''
# 递归， 时间复杂度为O(2^n)
def f1(n):
    if n == 1: return 1
    if n == 2: return 2
    return f1(n-1) + f1(n-2)

'''
n个台阶的走法f(n) = n-1个台阶的走法f(n-1) + n-2个台阶的走法f(n-2)
所以可以优化算法
'''
# 动态规划, 时间复杂度O(n), 空间复杂度O(1)
def f2(n):
    if n == 1: return 1
    if n == 2: return 2
    a, b = 1, 2
    temp = a + b
    for i in range(3, n+1):
        temp = a + b
        a = b
        b = temp
    return temp

