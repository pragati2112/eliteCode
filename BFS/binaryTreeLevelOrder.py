from collections import deque


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.next = None
        self.val = item


def traverse(root):
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)

    return result


def reverseTraverse(root):
    result = deque()
    queue = deque()

    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()

            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        result.appendleft(current_level)

    return result


def zigzagTraverse(root):
    result = []

    queue = deque()
    queue.append(root)
    zigzag = True
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if zigzag == True:
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
            else:
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            zigzag = not zigzag
        result.append(current_level)

    return result


def averagesOfLevel(root):
    queue = deque()
    result = []

    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        average = sum(current_level) / len(current_level)
        result.append(average)

    return result


def minDepth(root):
    queue = deque()
    minTreeDept = 0
    queue.append(root)

    while queue:
        minTreeDept += 1
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()

            if not current_node.left and not current_node.right:
                return minTreeDept

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)


def find_successor(root, num):
    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft()
        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

        if current_node.val == num:
            break
    return queue[0] if queue else None


def connectSibling(root):
    queue = deque()
    queue.append(root)
    while queue:
        prev = None
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()

            if prev:
                prev.next = current_node
            prev = current_node

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)


def connectAllOrderLevel(root):
    queue = deque()
    queue.append(root)
    current_node = None
    prev = None
    while queue:
        current_node = queue.popleft()
        if prev:
            prev.next = current_node

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

        prev = current_node


def rightViewBinaryTree(root):
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        level_size = len(queue)

        for i in range(0, level_size):
            current_node = queue.popleft()

            # each level last node
            if i == level_size - 1:
                result.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return result


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(6)
    root.left.right = Node(8)
