class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)



def count_paths(root, target):
	stack = []
	paths = []
	stack.append([root, [root.val]])
	
	while len(stack) > 0:
		current, current_path = stack.pop()

		if current.left:
			stack.append([current.left, current_path + [current.left.val]])
		if current.right:
			stack.append([current.right, current_path + [current.right.val]])

		if not current.left and not current.right:
			all_paths = find_path(current_path, target)
			for path in all_paths:
				paths.append(path)
	return paths



# This is the same problem as:
# https://leetcode.com/problems/subarray-sum-equals-k/
def find_path(arr, target):
	ranges = {0: []}
	sum_so_far = 0

	paths = []
	for i in range(len(arr)):
		sum_so_far += arr[i]
		diff = sum_so_far - target

		if diff in ranges:
			valid_paths = [arr[val+1: i + 1] for val in ranges.get(diff)]
			for v in valid_paths:
				paths.append(v)

		if sum_so_far in ranges:
			tmp_path = ranges[sum_so_far]
			tmp_path.append(i)
			ranges[sum_so_far] = tmp_path
		else:
			ranges[sum_so_far] = [i]
	return paths





def main():  
	root = TreeNode(12)  
	root.left = TreeNode(7)  
	root.right = TreeNode(1)  
	root.left.left = TreeNode(4)  
	root.right.left = TreeNode(10)  
	root.right.right = TreeNode(5)  
	print("Tree has paths: " + str(count_paths(root, 11)))
main()