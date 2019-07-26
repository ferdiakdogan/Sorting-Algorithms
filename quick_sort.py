from random import randrange, shuffle


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def quick_sort(list, start, end):
    # this portion of list has been sorted
    if start >= end:
        return

    # select random element to be pivot
    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]
    # swap random element with last element in sub-lists
    swap(list, pivot_idx, end)
    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            swap(list, i, less_than_pointer)
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    swap(list, less_than_pointer, end)
    # recursively sort left and right sub-lists
    quick_sort(list, start, less_than_pointer - 1)
    quick_sort(list, less_than_pointer + 1, end)


# list = [5, 3, 1, 7, 4, 6, 2, 8]
# shuffle(list)
# print("PRE SORT: ", list)
# quick_sort(list, 0, len(list) - 1)
# print("POST SORT: ", list)


