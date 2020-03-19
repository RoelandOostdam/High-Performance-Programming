import time
from mpi4py import MPI
import numpy as np
import sys

def remove_multiples(sieve, k):
	n = len(sieve) # Max number to calculate
	i = sieve.index(1) # Iterator starting at first 1

	if rank==0:
		data = sieve
	else:
		data = None

	data = comm.bcast(data, root=0)
	while i*(rank)*k<n:
		data[i*(rank)*k] = 0
		i+=size

	# Gathering
	newData = comm.gather(data, root=0)
	print('asd',newData)
	if rank==0:
		result = []
		for x in range(0,len(newData[0])):
			add = 1
			for t in range(0,size):
				if newData[t][x] == 0:
					add=0
				if(add==0):
					break
			result.insert(len(result),add)
		return result

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
	print('result:',result)

# Driver code
if __name__ == '__main__':
	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	n = int(sys.argv[1])

	if rank==0:
		print("Running with n =", n)

	time_start = time.time()
	sieve = run(n)
	time_taken = round(time.time() - time_start, 2)
	print("Execution time:",str(time_taken)+'s')
	print('result:',(sieve))
