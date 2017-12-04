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