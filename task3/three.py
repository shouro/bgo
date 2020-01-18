class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def lca(x, y):
    '''
    This function will create a set of all ancestors
    of node x including x itself. Then, in second loop
    it visit all ancestors of y. The first ancestor of y
    that is an ancestor of x will be the first common ancestor.
    So, This works in O(n) both time and space.
    '''
    a_ancestors = set()
    while x:
        a_ancestors.add(x)
        x = x.parent
    while y:
        if y in a_ancestors:
            return y
        y = y.parent
    return None


def three():
    root = Node(1)

    root.left = Node(2)
    root.left.parent = root
    root.right = Node(3)
    root.right.parent = root

    root.left.left = Node(4)
    root.left.left.parent = root.left
    root.left.right = Node(5)
    root.left.right.parent = root.left

    root.left.left.left = Node(8)
    root.left.left.left.parent = root.left.left
    root.left.left.right = Node(9)
    root.left.left.right.parent = root.left.left

    root.right.left = Node(6)
    root.right.left.parent = root.right
    root.right.right = Node(7)
    root.right.right.parent = root.right

    node1 = root.right.left
    node2 = root.right.right

    node3 = root.right
    node4 = root.right.right

    nlist = [(node1, node2), (node3, node4)]

    for x, y in nlist:
        print(lca(x, y).value)


if __name__ == "__main__":
    three()
