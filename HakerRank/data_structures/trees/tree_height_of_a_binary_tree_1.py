# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Tree: Height of a Binary Tree
# problem url: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
# date: 9/12/2017
# python 2

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None

def height(root):
    if root is None:
        return -1
    l = height(root.left)
    r = height(root.right)
    return max(l, r) + 1
