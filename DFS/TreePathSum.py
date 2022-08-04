class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.next = None
        self.val = item


def treePathSum(root, sum=10):
    if root.val==sum and not root.right and not root.left:
        return True
    
    return treePathSum(root.left, sum-root.val) or treePathSum(root.right, sum-root.val)    


# def allPathsForSum(root, sum=10):
#     result = []

#     if root.val==sum and not root.right and not root.left:
#         result.append(root.val)

#     treePathSum(root.left, sum-root.val) or treePathSum(root.right, sum-root.val)   





if __name__ == '__main__':

    root = Node(1)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(6)
    root.left.right = Node(8)
