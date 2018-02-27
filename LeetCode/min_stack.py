# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Min Stack
# problem url: https://leetcode.com/problems/min-stack/description/

class MinStack:
    def __init__(self):
        self.elements = []
        self.min_value = None

    def push(self, x):
        if len(self.elements) == 0:
            self.min_value = x
            self.elements.append(x)
        elif x < self.min_value:
            self.elements.append((2 * x) - self.min_value)
            self.min_value = x
        else:
            self.elements.append(x)

    def pop(self):
        if self.elements[-1] < self.min_value:
            self.min_value = 2 * self.min_value - self.elements[-1]
        self.elements.pop()

    def top(self):
        if self.elements[-1] <= self.min_value:
            return self.min_value
        else:
            return self.elements[-1]

    def getMin(self):
        return self.min_value
