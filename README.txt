1 - Bubble Sort:
Bubble sort is an algorithm to sort a list through repeated swaps of 
adjacent elements. It has a runtime of O(n^2).

For nearly sorted lists, bubble sort performs relatively few operations 
since it only performs a swap when elements are out of order.

Bubble sort is a good introductory algorithm which opens the door to 
learning more complex algorithms. It answers the question, “How can we 
algorithmically sort a list?” and encourages us to ask, “How can we 
improve this sorting algorithm?”

2 - Merge Sort:
Merge sort is a sorting algorithm created by John von Neumann in 1945. 
Merge sort’s “killer app” was the strategy that breaks the 
list-to-be-sorted into smaller parts, sometimes called a divide-and-conquer 
algorithm.

In a divide-and-conquer algorithm, the data is continually broken down 
into smaller elements until sorting them becomes really simple.

Merge sort was the first of many sorts that use this strategy, and is 
still in use today in many different applications.

3 - Quick Sort:
Quicksort is an efficient algorithm for sorting values in a list. A 
single element, the pivot, is chosen from the list. All the remaining 
values are partitioned into two sub-lists containing the values smaller 
than and greater than the pivot element.

Ideally, this process of dividing the array will produce sub-lists of 
nearly equal length, otherwise, the runtime of the algorithm suffers.

When the dividing step returns sub-lists that have one or less elements, 
each sub-list is sorted. The sub-lists are recombined, or swaps are made 
in the original array, to produce a sorted list of values.

4 - Radix Sort:

- A radix is the base of a number system. For the decimal number system, 
the radix is 10.
- Radix sort has two variants - MSD and LSD
- Numbers are bucketed based on the value of digits moving left to right 
(for MSD) or right to left (for LSD)
- Radix sort is considered a non-comparison sort
- The performance of radix sort is O(n)