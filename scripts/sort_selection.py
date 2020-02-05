from typing import List


def selection_sort(data: List[int]) -> None:
    """Sort an array using selection sort"""
    # loop over len(data) -1 elements
    for index1 in range(len(data)-1):
        smallest = index1 # first index of remaining array

        # loop to find index of smallest element
        for index2 in range(index1 + 1, len(data)):
            if data[index2] < data[index1]:
                smallest = index2

        # swap smallest element into position
        data[smallest], data[index1] = data[index1], data[smallest]


def recursive_selection_sort(data: List[int]) -> None:
    # Lists with less than one element are sorted
    if len(data) <= 1:
        return data
    else:
        smallest = min(data)    # find the smallest element in the list
        data.remove(smallest)   # remove from the list
        return [smallest] + recursive_selection_sort(data) # put on front of to be sorted remainder