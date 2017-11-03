# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Stacks: Simple Text Editor
# problem url: https://www.hackerrank.com/challenges/simple-text-editor/problem
# date: 9/12/2017

class Stack:
    def __init__(self):
        self._stack = []
        self._long = 0
        self._eliminates_values = []
        self._undo = []

    def push(self, value):
        self._stack.append(value)
        self._long += 1
        self._undo.append(0)

    def pop(self):
        self._long -= 1
        self._undo.append(1)
        self._eliminates_values.append(self._stack[-1])
        self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def empty(self):
        return self._long == 0

    def clear(self):
        self._stack = []
        self._long = 0        
        self._eliminates_values = []
        self._undo = []

    def undo(self):
        if self._undo[-1] == 0:
            self._undo.pop()
            self._stack.pop()
        elif self._undo[-1] == 1:
            self._undo.pop()
            self._stack.append(self._eliminates_values[-1])
            self._eliminates_values.pop()
            
            
            
            
stack = Stack()
count_undo = []
for i in range(int(input())):
    operation = input().split()
    if operation[0] == "1":
        count_undo.append(len(operation[1]))
        for j in range(len(operation[1])):
            stack.push(operation[1][j])
    elif operation[0] == "2":
        count_undo.append(int(operation[1]))
        for j in range(int(operation[1])):
            stack.pop()
    elif operation[0] == "3":
        print(stack._stack[int(operation[1])-1])
    elif operation[0] == "4":
        for j in range(count_undo[-1]):
            stack.undo()
        count_undo.pop()