"""
====================
Insertion Sort

Input:              sequence of *unsorted numbers
Output:             reordered sequence in non-decreasing order
Time Complexity     O(n^2)?
====================
"""
import random
import sys
import time


def insertion_sort(array):
    for j, key in enumerate(array[1:], start=1):
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array


def main():
    # TODO
    # account for duplicates
    # get input from command line args

    # random order
    # input_array = [5, 4, 3, 6, 7, 9]

    # acending order
    # input_array = [3, 4, 5, 6, 7, 9]

    # decending order
    input_array = [9, 7, 6, 5, 4, 3]

    start_time = time.time()
    sorted_input_array = insertion_sort(input_array)
    end_time = time.time()

    print(sorted_input_array)
    print("Time elapsed: " + str(end_time - start_time))


if __name__ == "__main__":
    main()
