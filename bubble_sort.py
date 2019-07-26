import numpy as np
import matplotlib.pyplot as plt
import cv2
import time


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    iterations = 0
    x = list(range(1000))
    height, width, channels = (500, 1000, 3)
    my_array = np.zeros((height, width, channels), np.uint8)
    rgb_color = (255, 255, 255)
    my_array[:] = rgb_color
    for j in range(1, len(arr) * 10, 10):
        cv2.rectangle(my_array, (j, height), (j + 10, height - arr[j//10] // 2), (0, 0, 0), 2)
    cv2.rectangle(my_array, (0, height), (0 + 10, height - arr[0] // 2), (0, 0, 255), 2)
    cv2.imwrite('pic.png', my_array)
    '''plt.figure(1)
    x = np.arange(1, len(arr))
    plt.bar(x, height=arr[1:], color='blue')
    plt.bar(0, height=arr[0], color='red')
    plt.savefig('pic.png')'''
    for element in arr:
        for i in range(len(arr) - 1):
            iterations += 1
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                my_array = np.zeros((height, width, channels), np.uint8)
                rgb_color = (255, 255, 255)
                my_array[:] = rgb_color
                for j in range(0, len(arr) * 10, 10):
                    cv2.rectangle(my_array, (j, height), (j + 10, height - arr[j//10] // 2), (0, 0, 0), 2)
                cv2.rectangle(my_array, ((i + 1)*10, height), ((i + 1)*10 + 10, height - arr[i + 1] // 2), (0, 0, 255), 2)
                cv2.imwrite('pic.png', my_array)
                '''x = np.arange(0, len(arr))
                plt.bar(x, height=arr, color='blue')
                plt.bar(i + 1, height=arr[i], color='red')
                plt.savefig('pic.png')'''

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


# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# bubble_sort_unoptimized(arr.copy())
# bubble_sort_optimized(arr)
# print(arr)

# arr = [3, 2, 17, 6, 4, 4, 9, 12, 1]
# bubble_sort_unoptimized(arr.copy())
# bubble_sort_optimized(arr)
# print(arr)



