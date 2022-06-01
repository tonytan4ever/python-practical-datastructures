'''
Naive O(m * n) implementation, like double pointer
https://leetcode.com/problems/implement-strstr/
'''


def strStr(hayStack, needle):
    if hayStack is None or needle is None:
        return -1

    m, n = len(needle), len(hayStack)

    for i in range(n):
        cur = i
        j = 0
        while cur < n and j < min(m, n) and needle[j] == hayStack[cur]:
            j += 1
            cur += 1
        
        if j == m:
            return i

    return -1
