def partition(arr, pivot):
	l1, l2 = [], []
	for x in arr[:-1]:
		if(x<pivot):
			l1.append(x)
		else:
			l2.append(x)
	return l1, l2

def quicksort(arr):
	if(len(arr)<2):
		return arr
	pivot = arr[-1]
	l1, l2 = partition(arr, pivot)
	return quicksort(l1) + [pivot] + quicksort(l2)


arr = [6, 5, 8, 44, 9, 17, 25, 11, 65, 234, 236, 87, 32, 45, 893, 752]
print(quicksort(arr))
