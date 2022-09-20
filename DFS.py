class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def IterativePreOrder(root):
    #### for iterative port order just reverse the output use python reverse() ######

    stack, output = [], []
    stack.append(root)
    while len(stack) > 0 and root is not None:
        node = stack.pop()
        output.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return output


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(6)
    root.left.right = Node(8)

    print(IterativePreOrder(root))
