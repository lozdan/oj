# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Binary Search Tree : Insertion
# problem url: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

def insert(r, val):
    if not r:
        return Node(val)
    node = r
    while True:
        if val < node.data:
            if not node.left:
                node.left = Node(val)
                break
            node = node.left
        else:
            if not node.right:
                node.right = Node(val)
                break
            node = node.right
    return r