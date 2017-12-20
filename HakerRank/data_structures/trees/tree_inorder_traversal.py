# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Tree: Height of a Binary Tree
# problem url: https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
# date: 9/12/2017
# python 2

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print root.data,
    inOrder(root.right)
