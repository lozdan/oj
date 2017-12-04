def levelOrder(root):
    def traverse(root_node, level):
        if not root_node:
            return []
        output = [(root_node.data, level)]
        l = traverse(root_node.left, level + 1)
        r = traverse(root_node.right, level + 1)
        return l + output + r
    answer = sorted(traverse(root, 0), key=lambda k: k[1])
    for node, _ in answer:
        print node,