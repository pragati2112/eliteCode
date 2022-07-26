def intersection(a_inertvals, b_intervals):
	result = []
	i, j,start,end = 0,0,0,1

	while i<len(a_inertvals) and j<len(b_intervals):

		a_overlaps_b = a_inertvals[i][start]>=b_intervals[j][start] and a_inertvals[i][start]<=b_intervals[j][end]
		b_overlaps_a = a_inertvals[i][start]<=b_intervals[j][start] and b_inertvals[j][start]<=a_intervals[i][end]

		if b_overlaps_a or a_overlaps_b:
			result.append([max(a_inertvals[i][start], b_intervals[j][start]),
			 min(a_inertvals[i][end], b_intervals[j][end])])


		if a_inertvals[i][end]<b_intervals[j][end]:
			i+=1
		else:
			j+=1

	return result			