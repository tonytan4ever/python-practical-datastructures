'''
KMP substring strStr implementation, 
Average: O(m + n) time complexity
'''
import random


def strStr(hayStack, needle):
    if hayStack is None or needle is None:
        return -1

    m, n = len(needle), len(hayStack)

    if m == 0:
        return 0

    mod, base = random.randint(1000000, 2000000), 31
    power, h, cur_h= 1, 0, 0

    # target (needle) hash code
    for i in range(min(m, n)):
        h = (h * base + ord(needle[i])) % mod
        cur_h = (cur_h * base + ord(hayStack[i])) % mod
        power = (power * base) % mod
    
    if cur_h == h and hayStack[:m] == needle:
        return 0

    # Sliding window
    for i in range(m, n):
        # abc + d
        cur_h = (cur_h * base + ord(hayStack[i])) % mod

        # abcd - a
        cur_h = (cur_h - power * ord(hayStack[i - m])) % mod
        if cur_h < 0:
            cur_h += mod

        if i >= m - 1 and cur_h == h:
            if hayStack[i - m + 1: i + 1] == needle:
                return i - m + 1

    return -1


assert strStr("hayStack", "needle") == -1
assert strStr("hayStack", "yStack") == 2
assert strStr("hello", "ll") == 2
assert strStr("aaaaa", "bba") == -1
assert strStr("a", "a") == 0
assert strStr("aaa", "a") == 0
assert strStr("aaa", "aaaa") == -1
