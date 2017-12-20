# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Print in Reverse
# problem url: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
# date: 9/3/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
class Stack:
    def __init__(self):
        self._stack = []
        self._long = 0
        self._eliminates_values = []
        self._undo = []
        self._sum = 0

    def push(self, value):
        self._sum += value
        self._stack.append(value)
        self._long += 1
        self._undo.append(0)

    def pop(self):
        self._sum -= self._stack[-1]
        self._long -= 1
        self._undo.append(1)
        self._eliminates_values.append(self._stack[-1])
        self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def empty(self):
        return self._long == 0


def ReversePrint(head):
    if head is None:
        return False
    else:
        stack = Stack()
        current = head
        while current is not None:
            stack.push(current.data)
            current = current.next
        while not stack.empty():
            print(stack.peek())
            stack.pop()