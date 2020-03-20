import time
import math
from mpi4py import MPI
import numpy as np
import sys

def remove_multiples(sieve, k):
	n = len(sieve) # Max number to calculate
	i = sieve.index(1) # Iterator starting at first 1

	# --------------------------------
	# TODO: optimized version
	# if rank==0:
	# 	data = np.array_split(sieve, comm.size)
	# else:
	# 	data = None
	#
	# b_data = comm.scatter(data, root=0)
	# print(rank,b_data)
	# sys.stdout.flush()
	#
	# while i*(rank+1)*k<n:
	# 	b_data[i*(rank+1)*k] = 0
	# 	i+=1
	# --------------------------------

	# --------------------------------
	# # Working prototype 1 (non-optimized)

	if rank==0:
		data = sieve
	else:
		data = None
	b_data = comm.bcast(data, root=0)
	while i*(rank+1)*k<n:
		b_data[i*(rank+1)*k] = 0
		i+=1
	# --------------------------------

	return b_data


def run(n):
	sieve = [1]*(n+1) # Initialize sieve
	sieve[0], sieve[1] = 0, 0 # 0 & 1 are not prime numbers
	k = 2
	while k<=math.sqrt(n)+1:
		# print(rank,"executing run",k)
		sieve = remove_multiples(sieve, k)
		k+=1
		try:
			k = sieve[k:].index(1)+k
		except:
			break
	return sieve

def next_k(sieve, k):
	if k==0:
		return 2
	k+=1
	k = sieve[k:].index(1)+k
	return k

def print_sieve(sieve):
	result = []
	for i, x in enumerate(sieve):
		if(x==1):
			result.append(i)
	print('result:',result)

# Driver code
if __name__ == '__main__':
	n = int(sys.argv[1])
	sieve = [1]*(n+1) # Initialize sieve
	sieve[0], sieve[1] = 0, 0 # 0 & 1 are not prime numbers
	tt = 0

	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	# Initialize sieve
	k = 0

	if rank==0:
		print("Running with n =", n)
		time_start = time.time()
		sys.stdout.flush()

	while k<math.sqrt(n):
		if rank==0:
			k = next_k(sieve,k)
		k = comm.bcast(k, root=0)
		# print(rank,k)
		# print(rank,k)
		# sys.stdout.flush()
		# comm.Barrier()

		result = remove_multiples(sieve,k)
		# comm.Barrier()

		gathered = comm.gather(result, root=0)

		if rank == 0:
			ts = time.time()
			result = []
			for x in range(0, len(gathered[0])):
				add = 1
				for t in range(0, size):
					if gathered[t][x] == 0:
						add = 0
					if (add == 0):
						break
				result.insert(len(result), add)
			tt += time.time() - ts

		sieve = comm.bcast(result, root=0)

	if rank==0:
		# sieve = run(n)
		time_taken = round(time.time() - time_start, 2)
		print("Total execution time:",str(time_taken)+'s')
		print("Waarvan domme functie time:", round(tt,2),'s')
		print('result:',(sieve))
		print_sieve(sieve)
