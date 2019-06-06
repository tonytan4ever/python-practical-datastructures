
class BinaryIndexTree:
    def __init__(self, n):
        self.x = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def update(self, i, v):
        while i < len(self.x):
            self.x[i] += v
            i += self.lowbit(i)

    def query(self, i):
        res_sum = 0
        while i > 0:
            res_sum += self.x[i]
            i -= self.lowbit(i)
        return res_sum
