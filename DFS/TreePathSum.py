class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.next = None
        self.val = item


def treePathSum(root, _sum=10):
    if root.val == _sum and not root.right and not root.left:
        return True

    return treePathSum(root.left, _sum - root.val) or treePathSum(root.right, _sum - root.val)


def allPathsForSum(root, _sum, current_path, all_paths):
    if root is None:
        return

    current_path.append(root.val)

    if root.val == _sum and root.right is None and root.left is None:
        all_paths.append(list(current_path))
    else:
        allPathsForSum(root.left, _sum - root.val, current_path, all_paths)
        allPathsForSum(root.right, _sum - root.val, current_path, all_paths)

    del current_path[-1]


def count_paths_for_sum(root, _sum, current_path):
    current_path.append(root.val)
    pathSum, pathCount = 0, 0
    for i in range(len(current_path) - 1, -1, -1):
        pathSum += current_path[i]
        if pathSum == _sum:
            pathCount += 1

    pathCount += count_paths_for_sum(root.left, _sum, current_path)
    pathCount += count_paths_for_sum(root.right, _sum, current_path)
    del current_path[-1]

    return pathCount


def find_sequence(root, seq, seq_index=0):
    if root.val != seq[seq_index]: return False

    if root.left is None and root.right is None and seq_index == len(seq) - 1:
        return True

    return find_sequence(root.left, seq, seq_index + 1) or find_sequence(root.right, seq, seq_index + 1)


def find_path_sum(root, pathSum):
    pathSum = 10 * pathSum + root.val

    if root.left is None and root.right is None:
        return pathSum

    return find_path_sum(root.left, pathSum) + find_path_sum(root.right, pathSum)


def dfsTraversal(root):
    stack = []
    stack.append(root)
    while stack:
        current_node = stack.pop()
        print(current_node.val)

        if current_node.right:
            stack.append(current_node.right)

        if current_node.left:
            stack.append(current_node.left)


if __name__ == '__main__':
    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(4)
    root.right.left = Node(10)
    root.right.right = Node(5)


    def find_paths():
        all_paths = []
        allPathsForSum(root, 23, [], all_paths)
        # print(all_paths)


    find_paths()
