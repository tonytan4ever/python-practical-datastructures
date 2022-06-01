'''
KMP substring strStr, O(m + n) time complexity
'''

def get_prefix_table(target, n):
    # get the prefix table
    prefix_table = [0] * (n + 1)
    prefix_table[0] = -1

    # matching target or target
    i, j = 0, -1
    while i < len(target):
        if j == -1 or target[i] == target[j]:
            i += 1
            j += 1
            # assign prefix of longest 
            prefix_table[i] = j
        else:
            # move pointer on target
            j = prefix_table[j]
    
    return prefix_table


def strStr(haystack: str, needle: str) -> int:
        # write your code 
    if haystack is None or needle is None:
        return -1
    
    if not needle:
        return 0
    
    if not haystack or len(haystack) < len(needle):
        return -1

    prefix_table = get_prefix_table(needle, len(needle))

    i, j = 0, 0
    while i < len(haystack) and j < len(needle):
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            # move pointer on target
            j = prefix_table[j]
    
    # key point 3: return the starting index of the match
    return i - j if j == len(needle) else -1


assert strStr("hayStack", "needle") == -1
assert strStr("hayStack", "yStack") == 2
assert strStr("hello", "ll") == 2
assert strStr("aaaaa", "bba") == -1
