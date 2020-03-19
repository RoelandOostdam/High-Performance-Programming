import time

def remove_multiples(sieve, k):
	n = len(sieve) # Max number to calculate
	i = sieve.index(1) # Iterator starting at first 1
	while i*k<n:
		sieve[i*k] = 0
		i+=1
	return sieve

def run(n):
	sieve = [1]*(n+1) # Initialize sieve
	sieve[0], sieve[1] = 0, 0 # 0 & 1 are not prime numbers
	k = 2
	while k<=n:
		sieve = remove_multiples(sieve, k)
		k+=1
		try:
			k = sieve[k:].index(1)+k
		except:
			break
	return sieve

def print_sieve(sieve):
	result = []
	for i, x in enumerate(sieve):
		if(x==1):
			result.append(i)
	print(result)

# Driver code
if __name__ == '__main__':
	n = 30
	print("Running with n =", n)
	time_start = time.time()
	sieve = run(n)
	time_taken = round(time.time() - time_start, 2)
	print("Execution time:",str(time_taken)+'s')
	print_sieve(sieve)
