def distribution_pass(arr, digits_from_right):
	bucket_arr = [
		[], [], [], [], [], [], [], [], [], []
	]
	for x in arr:
		bucket_arr[int(str(x)[len(str(x))-(digits_from_right+1)])].append(x)

	return bucket_arr

def gathering_pass(arr):
	og_arr = []
	for x in arr:
		for y in x:
			og_arr.append(y)
	return og_arr

def bucket_sort(arr):
	for i in range(0, 3):
		arr = distribution_pass(arr, i)
		arr = gathering_pass(arr)
	return arr

arr = [97, 7, 100, 4, 54, 85]
arr = distribution_pass(arr, 0)
arr = gathering_pass(arr)
arr = distribution_pass(arr, 1)
# arr = gathering_pass(arr)
print(arr)
# print(bucket_sort(arr))