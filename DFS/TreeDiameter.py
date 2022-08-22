class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.next = None
        self.val = item


def calculate_height(root, tree_diameter):
	left_tree_height = calculate_height(root.left, tree_diameter)
	right_tree_height = calculate_height(root.right, tree_diameter)

	diameter = left_tree_height + right_tree_height+2

	tree_diameter = max(tree_diameter, diameter)

	return max(left_tree_height, right_tree_height)+1


def pathWithMaxSum(root):
	left_tree = pathWithMaxSum(root.left)
	right_tree = pathWithMaxSum(root.right)

	left_tree = max(left_tree, 0)
	right_tree = max(right_tree, 0)

	local_sum = left_tree+right_tree+root.val
	global_sum = max(local_sum, global_sum)

	return max(left_tree, right_tree)+root.val



if __name__ == '__main__':

    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(4)
    root.right.left = Node(10)
    root.right.right = Node(5)

    def find_diameter(root):
    	tree_diameter = 0
        calculate_height(root, tree_diameter)
        return tree_diameter

    
    def find_path_sum(root):
    	global_sum = 0
        pathWithMaxSum(root, global_sum)
        return global_sum    

    find_diameter()
    find_path_sum()