def findAllSubsets(arr):
	subsets = []
	subsets.append([])
	for j in arr:
		for i in range(len(subsets)):
			set = list(subsets[i])
			set.append(j)
			subsets.append(set)

	return subsets



def findAllDistinctsSubsets(arr):
	subsets = []
	subsets.append([])
	for j in arr:
		for i in range(len(subsets)):
			set = list(subsets[i])
			set.append(j)
			if set not in subsets:
				subsets.append(set)

	return subsets


def permutations(arr):
	result = []
	permutations = []
	permutations.append([])
	for current_num in arr:
		print(permutations)
		for _ in range(len(permutations)):
			old_permut = permutations.pop(0)
			
			print('***', old_permut)
			for j in range(len(old_permut)+1):

				new_permut = list(old_permut)
				new_permut.insert(j, current_num)
				print('####', new_permut)

				if len(new_permut)==len(arr):
					result.append(new_permut)
				else:
					permutations.append(new_permut)	

	return result				




def stringChangeCasePermutations(s):
	result = []
	result.append(s)

	for i in range(len(s)):
		if s[i].isalpha():
			for j in range(len(result)):
				chs = list(result[j])
				print(chs)

				chs[i] = chs[i].swapcase()
				print('#########',chs)
				result.append(''. join(chs))	

	print(result)


class ParenthesisString:
	def __init__(self, str, openCount, closeCount):
		self.str = str
		self.open_count = openCount
		self.close_count = closeCount


def generateValidPerms(num):
	queue = []
	queue.append(ParenthesisString('', 0, 0))
	result = []

	while queue:
		current = queue.pop(0)

		if current.open_count == num and current.close_count == num:
			result.append(current)
		else:
			if current.open_count<num:
				queue.append(ParenthesisString(current.str+"(", current.open_count+1, current.close_count))	

			if current.open_count>current.close_count:
				queue.append(ParenthesisString(current.str+")", current.open_count, current.close_count+1))

	return result



print(stringChangeCasePermutations('ad72'))	