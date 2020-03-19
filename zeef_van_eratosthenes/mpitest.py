from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
n = 30

if rank == 0:
	sieve = range(0,30)
	data = list(np.array_split(sieve, size))
	print('we will be scattering:', data)
else:
	data = None

data = comm.scatter(data, root=0)
print('rank', rank, 'has data:', data)

newData = comm.gather(data,root=0)

if rank == 0:
	print('master:',newData)

	combined_arr = []
	for x in newData:
		combined_arr.insert(len(combined_arr),list(x))
	print(combined_arr)