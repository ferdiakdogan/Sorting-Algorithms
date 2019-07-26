import webbrowser
import os.path
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
from bubble_sort import bubble_sort_optimized, bubble_sort_unoptimized
from merge_sort import merge_sort
from radix_sort import radix_sort
from quick_sort import quick_sort


def main():
    path = os.getcwd()
    # open a web page with the image that refresh every second
    if os.path.exists(path + "/file.html") and os.path.exists(path + "/script.js"):
        webbrowser.open(path + "/file.html")
    else:
        print("\nPut the \".html\" and the \".js\" here: " + os.path.dirname(path))
        sys.exit()

    tobesorted = [random.randint(0, 1000) for i in range(100)]
    tobesorted = list(range(10, 1010, 10))
    random.shuffle(tobesorted)
    #cv2.imshow('img', my_array)
    #cv2.waitKey(0)
    bubble_sort_unoptimized(tobesorted)


if __name__ == "__main__":
    main()
