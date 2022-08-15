# def fib(n):
# 	fib.call_counter+=1
# 	if n<=1:
# 		return n	

# 	return fib(n-1)+fib(n-2)	

# fib.call_counter = 0

# print(fib(15))

# print(fib.call_counter)


hash_map = {}
def fib_with_dp(n):

	fib_with_dp.call_counter += 1

	if n in hash_map.keys():
		return hash_map[n]		

	if n<=1:
		return n	

	temp = fib_with_dp(n-1)+fib_with_dp(n-2)
	hash_map[n] = temp
	return temp


fib_with_dp.call_counter = 0

print(fib_with_dp(5))

print(fib_with_dp.call_counter)
print(hash_map)