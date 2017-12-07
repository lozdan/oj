def lca(root , v1 , v2):
    def ancestors(root, v):
        nodes = []
        while root.data != v:
            nodes.append(root)
            root = root.left if v < root.data else root.right
        nodes.append(root)
        return nodes

    ancestors_1 = reversed(ancestors(root, v1))
    ancestors_2 = set(ancestors(root, v2))

    for node in ancestors_1:
        if node in ancestors_2:
            return node