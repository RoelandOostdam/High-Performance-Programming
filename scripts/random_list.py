import random

def gen_list(n, verbose=False):
	if verbose:
		print("Generating list of size",n)
	return random.sample(range(0, n), n)