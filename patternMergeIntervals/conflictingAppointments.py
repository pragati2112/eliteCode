def intervals(intervals):
	start,end = 0,1
	intervals.sort(key=lambda x: x[start])

	for i in range(1, len(intervals)):
		if intervals[i][start]<intervals[i-1][end]:
			return False
	return True


def main():
	print(intervals([[1,4],[2,5],[7,9]]))
main()		