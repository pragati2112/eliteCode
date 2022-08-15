'''
In a grid of size m*n how many paths can you take to travel from top left cell to bottom right cell.
You can only move in right or bottom direction
a  b  c
d  e  f
You can go from a to f in following paths
a-->b-->c-->f
a-->d-->e-->f
a-->b-->e-->f

Total 3 paths

'''

def grid_travel(m,n): 
	grid_travel.call_counter+=1
	if m==1 and n==1:
		return 1

	if n==0 or m==0:
		return 0

	node_val = grid_travel(m-1, n) + grid_travel(m, n-1 )
	return node_val

grid_travel.call_counter = 0
print(grid_travel(5,5), grid_travel.call_counter)


hash_map = {}
def grid_travel(m,n): 
	grid_travel.call_counter+=1

	if str(m)+str(n) in hash_map.keys():
		return hash_map[str(m)+str(n)] 
		
	if m==1 and n==1:
		return 1

	if n==0 or m==0:
		return 0

	node_val = grid_travel(m-1, n) + grid_travel(m, n-1)
	hash_map[str(m)+str(n)] = node_val
	return node_val

grid_travel.call_counter = 0
print(grid_travel(5,5), grid_travel.call_counter)