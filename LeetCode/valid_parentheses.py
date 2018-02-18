# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Valid Parentheses
# problem url: https://leetcode.com/problems/valid-parentheses/description/

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

class Solution:
    def opposite(self, chatacter):
        if chatacter == ")":
            return "("
        elif chatacter == "]":
            return "["
        elif chatacter == "}":
            return "{"

    def isValid(self, s):
        stack = Stack()
        for i in range(len(s)):
            if s[i] in "([{":
                stack.push(s[i])
            elif stack._long > 0 and self.opposite(s[i]) == stack.peek():
                stack.pop()
            else:
                return False
        if stack._long == 0:
            return True
        return False
