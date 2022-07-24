def happyNumber(num):
	left, right = num, num
	while True:
		slow = find_sqaured_sum(slow)
		fast = find_sqaured_sum(find_sqaured_sum(fast))
		if slow==fast:
			break
	return slow ==1 		


	

def find_sqaured_sum(n):
	_sum = 0
	while n>0:
		digit = n%10
		_sum += digit*digit
		n = n//10
	return _sum	

print(happyNumber(23))	