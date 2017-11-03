# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Tree: Preorder Traversal
# problem url: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
# date: 9/12/2017
# python 2

def preOrder(root):
    if not root:
        return 
    print root.data,
    preOrder(root.left)
    preOrder(root.right)