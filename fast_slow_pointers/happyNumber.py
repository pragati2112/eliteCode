def happyNumber(num):
	num_arr = [int(x) for x in str(num)]
	left = 0
	

def find_sqaured_sum(n):
	_sum = 0
	while n>0:
		digit = n%10
		_sum += digit*digit
		n = n//10
	return _sum	

print(happyNumber(23))	