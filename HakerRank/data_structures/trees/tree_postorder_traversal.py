# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Tree: Postorder Traversal
# problem url: https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
# date: 9/12/2017
# python 2

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print root.data,