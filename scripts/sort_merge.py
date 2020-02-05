from typing import List

def merge_sort(data: List[int]) -> None:
    merge_sort2(data, 0, len(data)-1)

def merge_sort2(data: List[int], low: int, high: int) -> None:
    """Split data, sort subarrays and merge them into sorted array."""
    # test base case size of array equals 1
    if (high - low) >= 1: # if not base case
        middle1 = (low + high) // 2 # calculate middle of the array
        middle2 = middle1 + 1 # calculate next element over

        # split array in half then sort each half (recursive calls)
        merge_sort2(data, low, middle1) # first half of the array
        merge_sort2(data, middle2, high) # second half of the array

        # merge two sorted arrays after split calls return
        merge(data, low, middle1, middle2, high)

# merge two sorted subarrays into one sorted subarray
def merge(data: List[int], left: int, middle1: int, middle2: int, right: int) -> None:
    left_index = left # index into left subarray
    right_index = middle2 # index into right subarray
    combined_index = left # index into temporary working array
    merged = [0] * len(data) # working array

    # merge arrays until reaching end of either
    while left_index <= middle1 and right_index < right:
        # place smaller of two current elements into result
        # and move to next space in arrays
        if data[left_index] <= data[right_index]:
            merged[combined_index] = data[left_index]
            combined_index += 1
            left_index += 1
        else:
            merged[combined_index] = data[right_index]
            combined_index += 1
            right_index += 1

    # if left array is empty
    if left_index == middle2: # if True, copy in rest of right array
        merged[combined_index:right + 1] = data[right_index:right + 1]
    else: # right array is empty, copy in rest of left array
        merged[combined_index:right + 1] = data[left_index: middle1 + 1]

    data[left:right + 1] = merged[left:right + 1] # copy back to data


def merge_arrays(array1: List[int], array2: List[int]) -> List[int]:
    """Recursively merge two arrays into one sorted array"""
    if len(array1) == len(array2) == 0: # done when both arrays are empty
        return []
    else:
        if len(array1) == 0: # if either array is empty
            head, *tail = array2
            return [head] + merge_arrays(array1, tail) # merge the remainder of the non-empty list
        elif len(array2) == 0: # idem for the other array
            head, *tail = array1
            return [head] + merge_arrays(tail, array2)
        else: # when both still have elements
            head1, *tail1 = array1
            head2, *tail2 = array2
            if head1 < head2: # select the smallest
                return [head1] + merge_arrays(tail1, array2) # and merge with the remainder
            else:
                return [head2] + merge_arrays(array1, tail2) # idem for when array 2 had the smaller element


def recursive_merge_sort(data: List[int]) -> List[int]:
    """Recursive merge sort implementation for sorting arrays"""
    if len(data) == 1: # arrays with 1 element are sorted
        return data
    else:
        middle = int(len(data)/2) # find the middle (round down if len(data) is odd)
        first, second = data[:middle], data[middle:] # split the list in half
        return merge_arrays(recursive_merge_sort(first), recursive_merge_sort(second)) # merge_sort both arrays, and merge them into the result