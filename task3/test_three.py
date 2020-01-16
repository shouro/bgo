from unittest import main, TestCase
from three import Node, lca


class TestThree(TestCase):
    def test_three(self):
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

        prime = [3, 3]
        r = []
        for x, y in nlist:
            r.append(lca(x, y).value)
        self.assertEqual(prime, r)


if __name__ == '__main__':
    main()
