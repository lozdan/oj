# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Top View
# problem url: https://www.hackerrank.com/challenges/tree-top-view/problem

def topView(root):
    instance = root
    if not root:
        return
    answer = [instance.data]
    while instance.left:
        answer.append(instance.left.data)
        instance = instance.left
    answer.reverse()
    while root.right:
        answer.append(root.right.data)
        root = root.right
    print " ".join(map(str, answer))
