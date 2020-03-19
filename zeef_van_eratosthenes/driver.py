import matplotlib.pyplot as plt
import time
import sequential, parallel
from subprocess import Popen, PIPE

def run_test(tests, engine):
	global threads
	print("Running test with engine:",str(engine))
	results = {}
	for n in tests:
		print("Calculating n =",n)
		time_start = time.time()
		engine(n)
		time_taken = round(time.time() - time_start, 2)

		results[n] = time_taken
		print("Duration:",time_taken,'s')
	return results

def plot(results, title):
	lists = sorted(results.items())
	x, y = zip(*lists)
	plt.title("De Zeef van Eratosthenes")
	plt.xlabel("List size (n)")
	plt.ylabel("Execution time (s)")
	plt.xticks(x)
	plt.xlim(min(x), max(x))
	# plt.ylim(min(y), max(y))
	plt.plot(x, y, label=title)

def parallel_engine(n):
	global threads
	p = Popen(['run.bat', str(threads), 'parallel.py', str(n)], stdout=PIPE, stderr=PIPE)
	output, errors = p.communicate()
	p.wait()

# tests = [10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
# tests = [10000, 100000, 200000, 300000, 400000, 500000]
tests = [10000, 50000, 100000, 200000, 300000]

threads = 1;r_parallel_1 = run_test(tests, parallel_engine)
threads = 2;r_parallel_2 = run_test(tests, parallel_engine)
threads = 4;r_parallel_4 = run_test(tests, parallel_engine)
threads = 8;r_parallel_8 = run_test(tests, parallel_engine)
r_sequential = run_test(tests, sequential.run)
plot(r_sequential, "sequential")
plot(r_parallel_1, "parallel_1")
plot(r_parallel_2, "parallel_2")
plot(r_parallel_4, "parallel_4")
plot(r_parallel_8, "parallel_8")
plt.grid()
plt.legend()
plt.show()