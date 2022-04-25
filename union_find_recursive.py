'''
UnionFind is a disojoint data structure which supports:

O(lg*N) find
O(lg*N) union

very useful in graph, tree, and other set-union algorithms
This implementation use recursion for the find method

Created on April 24th, 2022

@author: tonytan4ever
'''


class UnionFind:

    def __init__(self):
        self.parents = {}
        # (TODO): Add union find customized logics here

    def find(self, x, path_compression=True):
        p = self.parents[x]
        if x != p:
            pp = self.find(p)
            self.parents[x] = pp
        return self.parents[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.parents[root_a] = root_b
            return True
        else:
            return False


if __name__ == '__main__':
    # (TODO): Add more tests here...
    pass
