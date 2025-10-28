class Node:
    def __init__(self, number=0, height=0):
        self.number = number
        self.height = height
        self.left = None
        self.right = None

    @staticmethod
    def insert(node, number):
        if number > node.number and node.right is None:
            node.right = Node(number, node.height + 1)
            return node.right.height
        elif number < node.number and node.left is None:
            node.left = Node(number, node.height + 1)
            return node.left.height
        elif number > node.number and node.right is not None:
            Node.insert(node.right, number)
        elif number < node.number and node.left is not None:
            Node.insert(node.left, number)

    @staticmethod
    def traverse(node)


if __name__ == "__main__":
    total = int(input())
    numbers = []
    for _ in range(total):
        numbers.append(int(input()))

    print()
    root = Node(numbers.pop(0))
    while numbers:
        print(Node.insert(root, numbers.pop(0)))
