import sys
reload(sys)
sys.setdefaultencoding('utf8')

def superEggDrop(K, N):
    """
    :type K: int
    :type N: int
    :rtype: int
    """
    mid = N
    count = 0
    while mid != 1:
        mid = mid/2
        count += 1
    return count + 2

print superEggDrop(1, 30)