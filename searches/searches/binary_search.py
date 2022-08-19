"""
Binary Search Algorithm.

input are numbers from command line args
expects a sorted list

test input is 1,3,5,7,9,11,13,14,16,18,19
"""

# Functions


def is_num_looking_for(current_position, num_looking_for):
    if current_position == num_looking_for:
        return True
    else:
        return False


def binary_search(array_of_nums, item_looking_for, low, high):

    # how long it took to find our number
    number_of_items_checked = 1
    found = None

    # need to check to see if we've exhausted our list.
    # check len of current list? something of that sort.

    if low > high:
        found = False
        return found

    elif len(array_of_nums) == 1:
        if array_of_nums[0] == item_looking_for:
            return True
        else:
            return False
    else:

        # going to converge on the number first
        midpoint_index = (low + high) // 2
        if is_num_looking_for(array_of_nums[midpoint_index], item_looking_for):
            found = True
            return found

        elif item_looking_for > array_of_nums[midpoint_index]:
            return binary_search(array_of_nums, item_looking_for, midpoint_index + 1, high)

        else:
            return binary_search(array_of_nums, item_looking_for, low, midpoint_index - 1)

    return found


# Main
def main():

    number_array = [1, 2, 3, 4, 5, 6, 7, 10]
    item_looking_for = 2
    size_of_list = len(number_array)
    midpoint_index = size_of_list // 2
    low = 0
    high = len(number_array) - 1
    item_in_list = binary_search(number_array, item_looking_for, low, high)
    print(item_in_list)
    # print("In list") if binary_search(number_array,
    #                                   item_looking_for, low, high) else print("not in list")


if __name__ == "__main__":
    main()
