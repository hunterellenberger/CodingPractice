class BST:
    def __init__(self, root=None, c=0):
        self.c = c
        self.root = root

    def insert(self, node, number):
        if number > node.number and node.right is None:
            node.right = Node(number, node.height + 1)
            self.c += node.right.height
        elif number < node.number and node.left is None:
            node.left = Node(number, node.height + 1)
            self.c += node.left.height
        elif number > node.number and node.right is not None:
            self.insert(node.right, number)
        elif number < node.number and node.left is not None:
            self.insert(node.left, number)

    def get_c(self):
        return self.c

    def get_root(self):
        return self.root

class Node:
    def __init__(self, number=0, height=0):
        self.number = number
        self.height = height
        self.left = None
        self.right = None


if __name__ == "__main__":
    total = int(input())
    numbers = []
    for _ in range(total):
        numbers.append(int(input()))

    root = Node(numbers.pop(0))
    bst = BST(root)
    print(str(bst.get_c()))
    while numbers:
        bst.insert(bst.get_root(), numbers.pop(0))
        print(str(bst.get_c()))
