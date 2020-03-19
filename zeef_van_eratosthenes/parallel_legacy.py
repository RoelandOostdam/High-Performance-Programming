import time
from mpi4py import MPI
import numpy as np
import sys

def remove_multiples(sieve, k):
	n = len(sieve) # Max number to calculate
	i = sieve.index(1) # Iterator starting at first 1

	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	while i*k<n:
		sieve[i*k] = 0
		i+=1
	return sieve

def run(n):
	# Initialize MPI
	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	# Initialize MPI data
	if rank == 0:
		sieve = [1]*(n+1) # Initialize sieve
		sieve[0], sieve[1] = 0, 0 # 0 & 1 are not prime numbers
		# data = np.array_split(sieve, size)
		data = sieve
	else:
		data = None

	# Scatter
	# data = list(comm.scatter(data, root=0))
	data = list(comm.bcast(data, root=0))
	# print('rank', rank, 'has data:', data)
	k = 2*(rank+1)
	while k<=n:
		sieve = remove_multiples(data, k)
		k+=size
		try:
			k = data[k:].index(1)+k
		except:
			break

	newData = comm.gather(data, root=0)
	if(rank==0):
		result = []
		cur_thread = 0
		for i in range(0,len(newData[0])):
			result.insert(len(result),newData[cur_thread][i])
			if(cur_thread+1<size):
				cur_thread+=1
			else:
				cur_thread=0
		print_sieve(result)
		return result

def print_sieve(sieve):
	result = []
	for i, x in enumerate(sieve):
		if(x==1):
			result.append(i)
	print(result)

# Driver code
if __name__ == '__main__':
	n = int(sys.argv[1])
	print("Running with n =", n)
	time_start = time.time()
	sieve = run(n)
	time_taken = round(time.time() - time_start, 2)
	print("Execution time:",str(time_taken)+'s')
