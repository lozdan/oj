# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Stacks: Balanced Brackets
# problem url: https://www.hackerrank.com/challenges/balanced-brackets/problem
# date: 9/9/2017

class Stack:
    def __init__(self):
        self._stack = []
        self._long = 0

    def push(self, value):
        self._stack.append(value)
        self._long += 1

    def pop(self):
        self._stack.pop()
        self._long -= 1

    def peek(self):
        return self._stack[-1]

    def empty(self):
        return self._long == 0

    def clear(self):
        self._stack = []
        self._long = 0
        
def balanced_brackets(sequence):
    stack = Stack()
    for i in range(len(sequence)):
        if sequence[i] in "([{":
            stack.push(sequence[i])
        elif not stack.empty() and opposite(sequence[i]) == stack.peek():
            stack.pop()
        else:
            return False
    return stack.empty()


def opposite(chatacter):
    if chatacter == ")":
        return "("
    elif chatacter == "]":
        return "["
    elif chatacter == "}":
        return "{"

n = int(input())
for i in range(n):
    s = input()
    if balanced_brackets(s):
        print("YES")
    else:
        print("NO")
    
