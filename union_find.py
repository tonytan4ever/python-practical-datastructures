'''
UnionFind is a disojoint data structure which supports:

O(lg*N) find
O(lg*N) union

very useful in graph, tree, and other set-union algorithms

Created on May 6, 2019

@author: tonytan4ever
'''


class UnionFind:

    def __init__(self):
        self.parents = {}
        # (TODO): Add union find customized logics here

    def find(self, x, path_compression=True):
        path = []
        while x != self.parents[x]:
            path.append(x)
            x = self.parents[x]

        if path_compression:
            for p in path:
                self.parents[p] = x

        return x

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
