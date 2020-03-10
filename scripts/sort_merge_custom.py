def merge(left, right):
	arr = []
	while len(left) > 0 or len(right) > 0:
		if (len(left) == 0):
			arr.append(right[0])
			right.pop(0)
			continue
		if (len(right) == 0):
			arr.append(left[0])
			left.pop(0)
			continue
		l0 = left[0]
		r0 = right[0]
		if l0 <= r0:
			arr.append(l0)
			left.pop(0)
		else:
			arr.append(r0)
			right.pop(0)
	return arr


def merge_sort2(arr):
	if len(arr) == 1:
		return arr

	l = len(arr) // 2
	left, right = arr[:l], arr[l:]
	return merge(merge_sort2(left), merge_sort2(right))


def merge_sort(arr):
	return merge_sort2(arr)
