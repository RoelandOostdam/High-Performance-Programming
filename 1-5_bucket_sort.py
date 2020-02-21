from scripts import random_list

def insertion_sort(alist):
	for i in range(1, len(alist)):

		# element to be compared
		current = alist[i]

		# comparing the current element with the sorted portion and swapping
		while i > 0 and alist[i - 1] > current:
			alist[i] = alist[i - 1]
			i = i - 1
		alist[i] = current

		# print(alist)

	return alist


def distribution_pass(arr, digits_from_left):
	bucket_arr = [
		[], [], [], [], [], [], [], [], [], []
	]

	for x in arr:
		if len(str(x)) <= digits_from_left:
			bucket_arr[len(str(x))].insert(0, x)
		else:
			bucket_arr[int(str(x)[len(str(x)) - (digits_from_left)])].append(x)

	return bucket_arr


def gathering_pass(arr):
	og_arr = []
	for x in arr:
		x = insertion_sort(x)
		for y in x:
			og_arr.append(y)
	return og_arr


def bucket_sort(arr):
	# print(0, "->", arr)
	for i in range(1, len(str(max(arr))) + 1):
		arr = distribution_pass(arr, i)
		arr = gathering_pass(arr)
		# print(i, "->", arr)
	return arr


# arr = [6, 5, 8, 44, 9, 17, 25, 11, 65, 234, 236, 87, 32, 45, 893, 752]
print(bucket_sort(random_list.gen_list(10000)))

# De complexiteit is gemiddeld O(n+k), waarbij k het maximaal aantal cijfers is in een getal.
# De worst-case scenario is O(n^2)
# Hoe meer ints in dezelfde bucket terecht komen, hoe langzamer dit algoritme
# Dit is getest met de PyCharm profile functie