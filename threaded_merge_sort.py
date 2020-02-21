from scripts.sort_merge_custom import merge_sort, merge
import scripts.random_list as random_list
import numpy as np
import concurrent.futures
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import time


def combine_threads(tracker):
	# TODO: This is not very efficient i know
	while len(tracker) > 1:
		tracker[0] = merge(tracker[0], tracker[1])
		tracker.pop(1)
	return tracker[0]


def threaded_merge(arr, threads):
	array_splits = np.array_split(arr, threads)
	tracker = []
	for t in range(0, threads):
		tracker.append([])
	with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
		for i, split in enumerate(array_splits):
			future = executor.submit(merge_sort, list(split))
			tracker[i] = future.result()
	return combine_threads(tracker)


arr = random_list.gen_list(10000)
threads = [1,2,4,8]
results = []
for t in threads:
	start_time = time.time()
	threaded_merge(arr, t)
	results.append(time.time() - start_time)

plt.xticks(threads)
plt.title("Time it takes to sort a list with multi-threading")
plt.xlabel("Threads")
plt.ylabel("Process duration (s)")
plt.tight_layout()
plt.grid()
plt.plot(threads, results)
plt.show()