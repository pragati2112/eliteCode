from collections import defaultdict

def dependency_order(num, orders):
	graph = defaultdict(list)
	indegrees = defaultdict()

	for order in orders:
		graph[order[0]].append(order[1])
		graph[order[1]].append(order[0])


	stack=[]
	visited=[]
	for node, val in graph.items():
		indegrees[node] = len(val)
		if len(val)==1:
			stack.append(node)

	while len(stack)>0:
		curr = stack.pop()
		visited.append(curr)

		for n in graph[curr]:
			indegrees[n]-=1
			if indegrees[n]==1:
				stack.append(n)

	if len(visited)==num:
		return visited
	else:
		return "Can't install package due to presence of cycle"


if __name__=='__main__':

	print(dependency_order(6, [['A', 'B'], ['B', 'C'], ['C', 'D'], ['C', 'E'], ['E', 'K']]))

	print(dependency_order(4, [['A', 'B'], ['B', 'C'], ['C', 'E'], ['C', 'B']]))


