# coding:utf-8
'''
对于两个字符串，请设计一个高效算法，求他们的最长公共子序列的长度，这里的最长公共子序列定义为有两个序列U1,U2,U3...Un和V1,V2,V3...Vn,其中Ui&ltUi+1，Vi&ltVi+1。且A[Ui] == B[Vi]。

给定两个字符串A和B，同时给定两个串的长度n和m，请返回最长公共子序列的长度。保证两串长度均小于等于300。

测试样例：

"1A2C3D4B56",10,"B1D23CA45B6A",12

返回：6

解析：https://github.com/imhuay/Algorithm_Interview_Notes-Chinese/blob/master/C-%E7%AE%97%E6%B3%95/%E4%B8%93%E9%A2%98-B-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.md#%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97lcs
'''


def findLCS( A, n, B, m):
        #result[i][j]保存A前i个子串和B前j个子串的公共子序列
        result = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                result[i][j] = max(result[i-1][j],result[i][j-1]) #默认传承之前的公共子序列长度
                if A[i-1]==B[j-1]:
                    result[i][j] = result[i-1][j-1]+1 #等于子串都减一的公共子序列长度加一
        return result[-1][-1]

a = findLCS("1A2C3D4B56",10,"B1D23CA45B6A",12)
print a