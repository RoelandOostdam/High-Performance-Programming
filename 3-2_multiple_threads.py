import logging
import threading
import time


def thread_function(name):
	logging.info("Thread %s: starting", name)
	time.sleep(2)  # wait for 2 seconds
	logging.info("Thread %s: finishing", name)


import concurrent.futures

if __name__ == "__main__":
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(thread_function, range(3))
