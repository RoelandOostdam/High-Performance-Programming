from mpi4py import MPI
import numpy as np
import sys
import math
from sequential import print_sieve

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 30

# Init sieve
sieve = [1]*(n+1)
sieve[0], sieve[1] = 0, 0

# K bepalen
def get_k(sieve,k):
	if k==0:
		return 2
	k = sieve[k:].index(1)+k
	return k

# Slicen
def slice(sieve):
	sliced_list = []
	for t in range(0,comm.size):
		sliced_list.append([])

	current_thread = 0
	for x in range(0,n):
		sliced_list[current_thread].append(sieve[x])
		if current_thread<comm.size-1:
			current_thread+=1
		else:
			current_thread=0
	return sliced_list

k = 2
k = get_k(sieve,k)

while k<=math.sqrt(n)+1:
	data = slice(sieve)[rank]
	