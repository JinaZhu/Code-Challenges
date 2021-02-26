# return a list of all characters that show up in all strings within the list (including duplicates).


def common_char(word_lst):
    previous_word = list(word_lst[0])

    for word in word_lst[1:]:
        current_word = []
        for char in word:
            if char in previous_word:
                current_word.append(char)
                previous_word.remove(char)
        previous_word = current_word

    return previous_word


print('common_char', common_char(
    ["bella", "label", "roller"]))

# An array is monotonic if it is either monotone increasing or monotone decreasing.


def is_monotonic(int_lst):
    for i in range(len(int_lst)-1):
        if int_lst[0] <= int_lst[-1]:
            if int_lst[i] <= int_lst[i+1]:
                continue
            else:
                return False

        if int_lst[0] >= int_lst[-1]:
            if int_lst[i] <= int_lst[i+1]:
                continue
            else:
                return False
        return True


print('is_monotonic', is_monotonic([3, 4, 2, 3]))

# Given an array, rotate the array to the right by k steps, where k is non-negative.


def rotateList(nums, steps):
    new_nums = nums[:]

    for i in range(len(nums)):
        if i >= len(nums) - steps:
            new_index = (i+steps) % len(nums)
            nums[new_index] = new_nums[i]
        else:
            nums[i+steps] = new_nums[i]
    return nums


print('rotateList', rotateList([1, 2, 3, 4, 5, 6, 7], 3))

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.


def plus_one(nums):
    # checking backward
    index = len(nums) - 1

    while index >= 0:
        # if the current index is 9, change it to 0
        if nums[index] == 9:
            nums[index] = 0
            index -= 1
        else:
            break
    # if index is -1, it means all the numbers are 9, so change first number to 1 and add another 0 to the end
    if index == -1:
        nums[0] = 1
        nums.append(0)
        return nums

    # whatever the current index is, add one
    nums[index] += 1

    return nums


print('plus_one', plus_one([1, 2, 3]))
print('plus_one', plus_one([9, 9, 9]))

# You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).


def rotate(matrix):
    for i in range(len(matrix)):
        # j should always start at index i
        for j in range(i, len(matrix[i])):
            # swap position
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


print('rotate', rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# Given an array of numbers, replace each even number with two of the same number.

def duplicate_even(nums):
    # loop through list, check for total of even nums
    # add even total empty spaces to the end of list
    # loop through the list backward with 2 pointers
        # fast pointer move ahead to check each item
        # slow pointer keep track of the location of swap position of num

    total_even = 0
    for num in nums:
        if num % 2 == 0:
            nums.append(-1)
            total_even += 1

    if total_even == 0:
        return nums
    
    slow = len(nums) -1
    fast = len(nums) -1

    while fast >= 0:
        if nums[fast] == -1:
            fast -= 1
        else: 
            if nums[fast] % 2 == 0:
                nums[slow] = nums[fast]
                slow -= 1

            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow -= 1
            fast -= 1
            
    return nums

# tescases to check: all even, all odds, single element, empty
duplicate_even_testcase = [1,2,5,6,8]
test_duplicate_even = duplicate_even(duplicate_even_testcase)
test_duplicate_result = test_duplicate_even == [1,2,2,5,6,6,8,8]
print('test_duplicate_result', test_duplicate_result)

duplicate_even_testcase_2 = [1,3,5,7,9]
test_duplicate_even_2 = duplicate_even(duplicate_even_testcase_2)
test_duplicate_result_2 = test_duplicate_even_2 == [1,3,5,7,9]
print('test_duplicate_result_2', test_duplicate_result_2)

# Given a sentence, reverse the words of the sentence.

def reverse_string(str):
    # loop through the string with two pointer backwards
        # fast will move to check for where the word start
        # slow will keep track of where the word end

    result = ""
    word = ""

    for char in str[::-1]:
        if char == " ":
            result += (word[::-1] + " ")
            word = ""
        else:
            word += char
    result += word[::-1]
    return result

reverse_string_testcase = "i live in a house"
test_reverse_string = reverse_string(reverse_string_testcase)
reverse_string_result = test_reverse_string == "house a in live i"

print('test_reverse_string', reverse_string_result)

# Given a sorted array in non-decreasing order, return an array of squares of each number, also in non-decreasing order.

def square_sorted_list(lst):
    # loop through the list with 2 pointers
        # start pointer and end pointer
    # square both pointer items
    # check which pointer is smaller and append in that order

    start = 0
    end = len(lst) -1
    change_index = len(lst) -1
    result = [0] * (change_index+1)

    while True:
        if start == end:
            result[change_index] = (lst[start]**2)
            return result
        elif abs(lst[start]) > abs(lst[end]):
            result[change_index] = (lst[start]**2)
            start += 1
        else:
            result[change_index] = (lst[end]**2)
            end -= 1
        change_index -= 1
            
# time complexity: O(n) -> only visiting items in list once
# space complexity: O(n) -> using space for result array

#cases to consider: empty list, list of 1, only positive or negative items
square_sorted_list_testcase = [-4,-2,-1,0,3,5] 
result_square_sorted_list = square_sorted_list(square_sorted_list_testcase)
square_sorted_list_test = result_square_sorted_list == [0,1,4,9,16,25]
print('square_sorted_list_test', square_sorted_list_test)

square_sorted_list_testcase_2 = [-4,-2,-1] 
result_square_sorted_list_2 = square_sorted_list(square_sorted_list_testcase_2)
square_sorted_list_test_2 = result_square_sorted_list_2 == [1,4,16]
print('square_sorted_list_test_2', square_sorted_list_test_2)

# Given an array of integers, find the continuous subarray, which when sorted, results in the entire array being sorted.

def shortest_unsorted_list(lst):
    # loop the list twice
        # once forward looking for the dip in the beginning
        # once backward looking for the dip in the end
    # find the max and min within the range
    # expand range to cover nums that falls with max and min

    front_dip = 0

    for i in range(1, len(lst)):
        if i == len(lst)-1:
            return []
        if lst[i] < lst[i-1]:
            front_dip = i-1
            break
    
    back_dip = 0
    
    for j in range(len(lst)-2, -1, -1):
        if lst[j] < lst[j+1]:
            back_dip = j
            break
    
    subarray = lst[front_dip:back_dip+1]
    max_of_subarray = max(subarray)
    min_of_subarray = min(subarray)

    for i in range(len(lst[:front_dip])):
        if lst[i] > min_of_subarray:
            front_dip = i
    
    for j in range(back_dip, len(lst)):
        if lst[j] < max_of_subarray:
            back_dip = j
    return(lst[front_dip:back_dip+1])


# time complexity: O(n) -> even through I have multiple loops, each loop has a time complexity of O(n)
# space complexity: O(n) -> using space for result subarray

# cases to consider: empty list, list of 1, when list is already in order
shortest_unsorted_list_testcase = [0,2,3,1,8,6,9]
shortest_unsorted_list_result = shortest_unsorted_list(shortest_unsorted_list_testcase)
shortest_unsorted_list_test = shortest_unsorted_list_result == [2,3,1,8,6]
print('shortest_unsorted_list_test', shortest_unsorted_list_test)

shortest_unsorted_list_testcase_2 = [1, 2, 3, 7, 5, 6, 8, 9]
shortest_unsorted_list_result_2 = shortest_unsorted_list(shortest_unsorted_list_testcase_2)
shortest_unsorted_list_test_2 = shortest_unsorted_list_result_2 == [7, 5, 6, 8]
print('shortest_unsorted_list_test_2', shortest_unsorted_list_test_2)


# Given an array with n marbles colored Red, White or Blue, sort them so that marbles of the same color are adjacent, with the colors in the order Red, White and Blue. Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).
def marbles_sort(lst):
    # loop through lst with three pointer, one at the end, one at the beginning, and one at the end
    # make sure the end and beginning pointer current item isn't 0 or 2
    # once begin and end is in right position move the middle pointer to swap 0s to the beginning and 2 to the end

    begin = 0
    end = len(lst) - 1
    middle = 0

    while middle <= end:
        if lst[begin] == 0:
            begin += 1
            middle = begin
            continue
        elif lst[end] == 2:
            end -= 1
            continue

        if lst[middle] == 0:
            lst[begin], lst[middle] = lst[middle], lst[begin]
            begin += 1
            middle += 1
        elif lst[middle] == 2:
            lst[end], lst[middle] = lst[middle], lst[end]
            end -= 1
        else:
            middle += 1
    return lst

# time complexity: O(n) -> looping through the list once
# space complexity: O(1) -> changing the original list 

# cases to consider: empty list, list with one single color
marbles_sort_testcase = [1, 0, 1, 2, 1, 0, 1, 2]
marbles_sort_result = marbles_sort(marbles_sort_testcase)
marbles_sort_test = marbles_sort_result == [0, 0, 1, 1, 1, 1, 2, 2]
print('marbles_sort_test', marbles_sort_test)

marbles_sort_testcase = [0, 0, 2, 1, 2, 1, 0, 1, 2]
marbles_sort_result = marbles_sort(marbles_sort_testcase)
marbles_sort_test = marbles_sort_result == [0, 0, 0, 1,1, 1, 2, 2, 2]
print('marbles_sort_test', marbles_sort_test)

marbles_sort_testcase = [2, 2, 2]
marbles_sort_result = marbles_sort(marbles_sort_testcase)
marbles_sort_test = marbles_sort_result == [2, 2, 2]
print('marbles_sort_test', marbles_sort_test)

# Given an array of integers, return the max sum of a continous subarray
def max_sum(nums):
    max_sum = nums[0]
    max_ending = nums[0]

    for i in range(1, len(nums)):

        current_sum = max_ending + nums[i]

        max_ending = max(current_sum, nums[i])
        max_sum = max(max_sum, max_ending)

    return max_sum

# time complexity: O(n) -> looping through the list once
# space complexity: O(1) 
max_sum_testcase = [1,2,-1,2,-3,2,-5]
max_sum_result = max_sum(max_sum_testcase)
max_sum_test = max_sum_result == 4
print('max_sum_test', max_sum_test)