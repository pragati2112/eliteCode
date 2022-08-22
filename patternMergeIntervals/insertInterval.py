def merge(intervals, new_interval):
	result = []
	start, end = 0,1

	# when intervals are sorted-----
	for i in range(len(intervals)):
		# non overlapping to the left
		if new_interval[end]<intervals[i][start]:
			result.append(new_interval)
			return result+intervals[i:]	

		# non overlapping to the right
		elif new_interval[start]>intervals[i][end]:
			result.append[intervals[i]]	

		# if overlapping
		else:
			new_interval = [min(new_interval[start], intervals[i][start]),
			 max(new_interval[end], new_interval[i][end])]	

	result.append(new_interval)
	return result			 
		



def main():
	print(merge([[1,3],[5,7], [8,12]], [4,6]))



main()				