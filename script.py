import random
import pygame

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


def merge_sort(items, start = 0, end = 499):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    py_mid = (start + end + 1) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]
    start = py_mid - middle_index
    end = py_mid
    left_sorted = merge_sort(left_split, start, end)
    for i in range(start, end):
        pygame.draw.rect(screen, (0, 0, 0), (i * w, 0, w - 1, y))
        pygame.display.update()
        pygame.draw.rect(screen, WHITE, (i * w, y - left_sorted[i - py_mid], w - 1, left_sorted[i - py_mid]))
        pygame.display.update()
    start = py_mid
    end = py_mid + middle_index
    right_sorted = merge_sort(right_split, start, end)
    for i in range(start, end):
        pygame.draw.rect(screen, (0, 0, 0), (i * w, 0, w - 1, y))
        pygame.display.update()
        pygame.draw.rect(screen, WHITE, (i * w, y - right_sorted[i - py_mid], w - 1, right_sorted[i - py_mid]))
        pygame.display.update()

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    if len(result) == 500:
        for x in range(len(result)):
            pygame.draw.rect(screen, (0, 0, 0), (x * w, 0, w - 1, y))
            pygame.display.update()
            pygame.draw.rect(screen, WHITE, (x * w, y - result[x], w - 1, result[x]))
            pygame.display.update()
    return result


def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    being_sorted = to_be_sorted[:]
    iterations = 0
    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        digits = [[] for i in range(10)]

        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
                digit = int(digit)
            except IndexError:
                digit = 0

            digits[digit].append(number)

            being_sorted = []
            iterations += 1
        for numeral in digits:
            being_sorted.extend(numeral)
        for x in range(len(being_sorted)):
            pygame.draw.rect(screen, (0, 0, 0), (x * w, 0, w - 1, y))
            pygame.display.update()
            pygame.draw.rect(screen, WHITE, (x * w, y - being_sorted[x], w - 1, being_sorted[x]))
            pygame.display.update()
        print(being_sorted)
        print("---------------------------------------")
    print("Process completed in {0} iterations.".format(iterations))
    return being_sorted


"""print("Welcome to sorting algorithms visualization...")
valid_choices = ["Bubble Sort Unoptimized", "Bubble Sort Optimized", "Quick Sort", "Merge Sort", "Radix Sort"]
[print(item) for item in valid_choices]
choice = input("\nWhich Algorithm do you want to see: ")
if choice not in valid_choices:
    print("please select from these algorithms: {0}".format(valid_choices))
else:
    print("\n*** You have chosen: {0} ***\n".format(choice))

choice = choice.lower().replace(" ", "_") """

# initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithms")
clock = pygame.time.Clock()

# initialize screen
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Welcome to Sorting Algorithm Visualization!', True, green, blue)
text2 = font.render('(Press mouse to continue)', True, red, (0, 0, 0))
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect.center = (width // 2, height // 2)
textRect2.center = (width // 2, 2 * height // 3)
screen.blit(text, textRect)
screen.blit(text2, textRect2)


# ##### pygame loop #######
running = True
state = "INITIAL"
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    pygame.display.update()
    # process input (events)
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0] and state is "INITIAL":
            screen.fill((0, 0, 0))
            text = font.render('Choose an algorithm to see: ', True, WHITE, (0, 0, 128))
            text2 = font.render('Bubble Sort Unoptimized', False, WHITE)
            text3 = font.render('Bubble Sort Optimized', False, WHITE)
            text4 = font.render('Quick Sort', False, WHITE)
            text5 = font.render('Merge Sort', False, WHITE)
            text6 = font.render('Radix Sort', False, WHITE)
            textRect = text.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect.center = (width // 2, 2 * height // 8)
            textRect2.center = (width // 2, 3 * height // 8)
            textRect3.center = (width // 2, 4 * height // 8)
            textRect4.center = (width // 2, 5 * height // 8)
            textRect5.center = (width // 2, 6 * height // 8)
            textRect6.center = (width // 2, 7 * height // 8)
            screen.blit(text, textRect)
            screen.blit(text2, textRect2)
            screen.blit(text3, textRect3)
            screen.blit(text4, textRect4)
            screen.blit(text5, textRect5)
            screen.blit(text6, textRect6)
            state = "READY"

        elif pygame.mouse.get_pressed()[0] and state is "READY":
            pos = pygame.mouse.get_pos()
            if textRect2.collidepoint(pos):
                screen.fill((0, 0, 0))
                tobesorted = initialize_array(500)
                init_screen(tobesorted)
                bubble_sort_unoptimized(tobesorted)
                state = "RUNNING"
            elif textRect3.collidepoint(pos):
                screen.fill((0, 0, 0))
                tobesorted = initialize_array(500)
                init_screen(tobesorted)
                bubble_sort_optimized(tobesorted)
                state = "RUNNING"
            elif textRect4.collidepoint(pos):
                screen.fill((0, 0, 0))
                tobesorted = initialize_array(500)
                init_screen(tobesorted)
                quick_sort(tobesorted)
                state = "RUNNING"
            elif textRect5.collidepoint(pos):
                screen.fill((0, 0, 0))
                tobesorted = initialize_array(500)
                init_screen(tobesorted)
                sorted = merge_sort(tobesorted)
                state = "RUNNING"
            elif textRect6.collidepoint(pos):
                screen.fill((0, 0, 0))
                tobesorted = initialize_array(500)
                init_screen(tobesorted)
                sorted = radix_sort(tobesorted)
                state = "RUNNING"
        elif state is "RUNNING":
            state = "INITIAL"

        # check for closing the window
        if event.type == pygame.QUIT:
            running = False


