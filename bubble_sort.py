
def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort(arr):
    for element in arr:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubble_sort(arr)
print(arr)

