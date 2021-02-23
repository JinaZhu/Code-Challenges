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
