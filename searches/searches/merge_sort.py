"""
=================================================
Author:        Drew Rinker
Date:          08/04/2022
Last Modifie:  08/04/2022

Description:   Insertion Sort Algorithm
               Runtime is O(n log n)
=================================================
"""
from re import A


def merge(left, right):

    combined_arr = []

    # i is left index marker
    # j is right index marker
    i = 0
    j = 0

    for k in range(len(left) + len(right)):

        # it's important for the left condition to stay on the left
        # it prevents an index out of range error when 'right' has had all items sorted
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            combined_arr.append(left[i])
            i += 1
        else:
            combined_arr.append(right[j])
            j += 1

    return combined_arr


def merge_sort(array):

    # base case
    if len(array) == 1:
        return array

    left = merge_sort(array[0:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    sorted_array = merge(left, right)
    return sorted_array


def main():
    # array of input
    unsorted_array = [3, 2, 7, 5, 9, 1, 6, 8, 4]
    sorted_array = merge_sort(unsorted_array)
    print(sorted_array)


if __name__ == "__main__":
    main()
