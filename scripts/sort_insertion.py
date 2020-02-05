from typing import List


def insertion_sort(data: List[int]) -> None:
    """Sorting an array in place using insertion sort."""
    # loop over len(data) - 1 elements
    for next in range(1, len(data)):
        insert = data[next] # value to insert
        move_item = next    # location to place element

        # search for place to put current element
        while move_item > 0 and data[move_item - 1] > insert:
            # shift element right one slot
            data[move_item] = data[move_item - 1]
            move_item -= 1

        data[move_item] = insert # place inserted element


def recursive_insertion_sort(toSort: List[int], sorted: List[int] = []) -> List[int]:
    """Recursive implementation of insertion sort"""
    if len(toSort) == 0: # empty lists are sorted
        return sorted
    else:
        head, *tail = toSort
        sorted = recursive_insertion(head, sorted) # insert the head into the sorted list
        return recursive_insertion_sort(tail, sorted) # recursive call to sort the remainder


def recursive_insertion(element: int, data: List[int]) -> List[int]:
    """Assistant function to recursive insertion sort; recursively insert into a list"""
    if len(data) == 0: # if the list is empty, the element should be place there anyway
        return [element]
    else:
        head, *tail = data
        if element < head: # when the element is smaller than the head of the insertion list
            return [element, head] + tail # place it on the front
        else:
            return [head] + recursive_insertion(element, tail) # else, keep the head separate, and recursively insert into the tail