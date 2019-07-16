
def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    iterations = 0
    for element in arr:
        for i in range(len(arr) - 1):
            iterations += 1
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
    print("Unoptimized bubble sort completed in: {0} iterations".format(iterations))


# We don't need to iterate all array at each time, only iterate until last sorted element

def bubble_sort_optimized(arr):
    iterations = 0
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            iterations += 1
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)
    print("Optimized bubble sort completed in: {0} iterations".format(iterations))


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort_unoptimized(arr.copy())
bubble_sort_optimized(arr)
print(arr)

arr = [3, 2, 17, 6, 4, 4, 9, 12, 1]
bubble_sort_unoptimized(arr.copy())
bubble_sort_optimized(arr)
print(arr)




