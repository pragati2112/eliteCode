class Node:
	def __init__(self, item):
		self.left = None
		self.right = None
		self.val = item


def inorder(self, root):
	if root:
		inorder(root.left)
		print(root.val + '-->')
		inorder(root.right)


def preorder(self, root):
	if root:
		print(root.val)
		preorder(root.left)
		preorder(root.right)
        

def postorder(self, root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.val)


# Checking full binary tree
def isFullTree(root):

    # Tree empty case
    if root is None:
        return True

    # Checking whether child is present
    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))

    return False




if __name__ == '__main__':

    root = Node(1)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(6)
    root.left.right = Node(8)

    print(inorder(root))
    print(preorder(root))
    print(postorder(root))




