'''
A monotonous stack is just like a stack, except all elements in it is
monotonously increasing or decreasing

Created on May 6, 2019

@author: tonytan4ever
'''


class MonotonousStack:

    def __init__(self,  has_pop_handler=False):
        self.stack = []
        self.has_pop_handler = has_pop_handler

    def push(self, target_val):
        while self.size > 0 and self.top >= target_val:
            val = self.pop()
            if self.has_pop_handler:
                self.pop_handler(val, target_val)
        self.stack.append(target_val)

    def pop(self):
        return self.stack.pop()

    @property
    def size(self):
        return len(self.stack)

    @property
    def top(self):
        if self.size > 0:
            return self.stack[-1]
        else:
            raise ValueError

    def pop_handler(self, val, target_val):
        raise NotImplemented


if __name__ == '__main__':
    pass
