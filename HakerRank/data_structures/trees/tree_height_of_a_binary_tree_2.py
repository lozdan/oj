# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Tree: Height of a Binary Tree
# problem url: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
# date: 9/14/2017
# python 2

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None

class Queue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._first_element = 0

    def enqueue(self, value):
        self._queue.append(value)
        self._count += 1

    def dequeue(self):
        if self._count > 0:
            self._first_element += 1
            self._count -= 1
        else:
            raise Exception("Empty array")

    def peek(self):
        if self._count > 0:
            return self._queue[self._first_element]
        else:
            raise Exception("Empty array")

    def empty(self):
        return self._count == 0

queue = Queue()
    
def height(root):
    if root is None:
        return 0
    else:
        queue.enqueue([root, 0])
        tall = 0
        while not queue.empty():
            current_node = queue.peek()
            if current_node[0].left:
                queue.enqueue([current_node[0].left, (current_node[1] + 1)])
            if current_node[0].right:
                queue.enqueue([current_node[0].right, (current_node[1] + 1)])
            queue.dequeue()
            tall = current_node[1]
        return tall