# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Trees: Tree: Level Order Traversal
# problem url: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

def levelOrder(root):
    queue = Queue()
    queue.enqueue(root)
    answer = [root.data]
    while not queue.empty():
        node = queue.peek()
        if node.left:
            queue.enqueue(node.left)
            answer.append(node.left.data)
        if node.right:
            queue.enqueue(node.right)
            answer.append(node.right.data)
        queue.dequeue()
    print " ".join(map(str, answer))