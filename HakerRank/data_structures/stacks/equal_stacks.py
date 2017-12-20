# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Stacks: Equal Stacks
# problem url: https://www.hackerrank.com/challenges/equal-stacks/problem
# date: 9/10/2017

class Stack:
    def __init__(self):
        self._stack = []
        self._long = 0
        self._height = 0

    def push(self, value):
        self._stack.append(value)
        self._long += 1
        self._height += value

    def pop(self):
        self._height -= self._stack[-1]
        self._stack.pop()
        self._long -= 1

    def peek(self):
        return self._stack[-1]

    def empty(self):
        return self._long == 0

    def clear(self):
        self._stack = []
        self._long = 0
        self._height = 0

    def height(self):
        return self._height
    
def convert_to_stack(arr):
    stack = Stack()
    for k in range(len(arr)-1, -1, -1):
        stack.push(arr[k])
    return stack


def determine_equality(data_1, data_2, data_3):
    values = [data_1.height(), data_2.height(), data_3.height()]
    if max(values) == data_1.height():
        data_1.pop()
    elif max(values) == data_2.height():
        data_2.pop()
    elif max(values) == data_3.height():
        data_3.pop()


cylinder_disks = [int(i) for i in input().split()]
cylinder_1 = convert_to_stack([int(i) for i in input().split()])
cylinder_2 = convert_to_stack([int(i) for i in input().split()])
cylinder_3 = convert_to_stack([int(i) for i in input().split()])

while not (cylinder_1.height() == cylinder_2.height() == cylinder_3.height()):
    determine_equality(cylinder_1, cylinder_2, cylinder_3)

print(cylinder_1.height())
