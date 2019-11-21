import random
import pygame
import time


# parameters
width = 1200
height = 600
FPS = 30
x = 0
y = height
w = 2

# colors
WHITE = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithms")
clock = pygame.time.Clock()


def initialize_array(length):
    tobesorted = list(range(1, 501, 1))
    random.shuffle(tobesorted)
    return tobesorted


def init_screen(tobesorted):
    for x in range(0, len(tobesorted) * w, w):
        pygame.draw.rect(screen, WHITE, (x, y - tobesorted[x // w], w - 1, tobesorted[x // w]))
        pygame.display.update()


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    iterations = 0
    count = len(arr)
    for element in arr:
        for i in range(len(arr) - 1):
            pygame.draw.rect(screen, red, (i * w, y - arr[i], w - 1, arr[i]))
            pygame.display.update()
            iterations += 1
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                pygame.draw.rect(screen, (0, 0, 0), (i * w, 0, w - 1, y))
                pygame.display.update()
                pygame.draw.rect(screen, WHITE, (i * w, y - arr[i], w - 1, arr[i]))
                pygame.display.update()
                pygame.draw.rect(screen, red, ((i + 1) * w, y - arr[i+1], w - 1, arr[i+1]))
                pygame.display.update()
            elif i < count - 1:
                pygame.draw.rect(screen, WHITE, (i * w, y - arr[i], w - 1, arr[i]))
                pygame.display.update()
            else:
                pygame.draw.rect(screen, blue, (i * w, y - arr[i], w - 1, arr[i]))
                pygame.display.update()
        count -= 1

    print("Unoptimized bubble sort completed in: {0} iterations".format(iterations))


# We don't need to iterate all array at each time, only iterate until last sorted element

def bubble_sort_optimized(arr):
    iterations = 0
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            pygame.draw.rect(screen, red, (idx * w, y - arr[idx], w - 1, arr[idx]))
            pygame.display.update()
            iterations += 1
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)
                pygame.draw.rect(screen, (0, 0, 0), (idx * w, 0, w - 1, y))
                pygame.display.update()
                pygame.draw.rect(screen, WHITE, (idx * w, y - arr[idx], w - 1, arr[idx]))
                pygame.display.update()
                pygame.draw.rect(screen, red, ((idx + 1) * w, y - arr[idx + 1], w - 1, arr[idx + 1]))
                pygame.display.update()
            else:
                pygame.draw.rect(screen, WHITE, (idx * w, y - arr[idx], w - 1, arr[idx]))
                pygame.display.update()
        pygame.draw.rect(screen, blue, ((idx + 1) * w, y - arr[idx + 1], w - 1, arr[idx + 1]))
        pygame.display.update()
    pygame.draw.rect(screen, blue, (x, y - arr[0], w - 1, arr[0]))
    pygame.display.update()
    print("Optimized bubble sort completed in: {0} iterations".format(iterations))


def quick_sort(lst, start=0, end=499):
    # this portion of list has been sorted
    if start >= end:
        return

    # select random element to be pivot
    pivot_idx = random.randrange(start, end)
    pivot_element = lst[pivot_idx]
    pygame.draw.rect(screen, red, (pivot_idx * w, y - lst[pivot_idx], w - 1, lst[pivot_idx]))
    pygame.display.update()
    # swap random element with last element in sub-lists
    swap(lst, pivot_idx, end)
    pygame.draw.rect(screen, (0, 0, 0), (pivot_idx * w, 0, w - 1, y))
    pygame.display.update()
    pygame.draw.rect(screen, (0, 0, 0), (end * w, 0, w - 1, y))
    pygame.display.update()
    pygame.draw.rect(screen, WHITE, (pivot_idx * w, y - lst[pivot_idx], w - 1, lst[pivot_idx]))
    pygame.display.update()
    pygame.draw.rect(screen, red, (end * w, y - lst[end], w - 1, lst[end]))
    pygame.display.update()
    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if lst[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            swap(lst, i, less_than_pointer)
            pygame.draw.rect(screen, (0, 0, 0), (i * w, 0, w - 1, y))
            pygame.display.update()
            pygame.draw.rect(screen, (0, 0, 0), (less_than_pointer * w, 0, w - 1, y))
            pygame.display.update()
            pygame.draw.rect(screen, WHITE, (i * w, y - lst[i], w - 1, lst[i]))
            pygame.display.update()
            pygame.draw.rect(screen, WHITE, (less_than_pointer * w, y - lst[less_than_pointer], w - 1, lst[less_than_pointer]))
            pygame.display.update()
            less_than_pointer += 1

    # move pivot element to the right-most portion of lesser elements
    swap(lst, less_than_pointer, end)
    pygame.draw.rect(screen, (0, 0, 0), (less_than_pointer * w, 0, w - 1, y))
    pygame.display.update()
    pygame.draw.rect(screen, (0, 0, 0), (end * w, 0, w - 1, y))
    pygame.display.update()
    pygame.draw.rect(screen, WHITE, (less_than_pointer * w, y - lst[less_than_pointer], w - 1, lst[less_than_pointer]))
    pygame.display.update()
    pygame.draw.rect(screen, WHITE, (end * w, y - lst[end], w - 1, lst[end]))
    pygame.display.update()
    # recursively sort left and right sub-lists
    quick_sort(lst, start, less_than_pointer - 1)
    quick_sort(lst, less_than_pointer + 1, end)


tobesorted = initialize_array(500)
init_screen(tobesorted)
quick_sort(tobesorted)

# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    pygame.display.update()
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False


