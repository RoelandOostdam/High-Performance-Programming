from scripts.sort_merge_custom import merge_sort, merge
import numpy as np
import concurrent.futures
import seaborn as sns; sns.set()


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