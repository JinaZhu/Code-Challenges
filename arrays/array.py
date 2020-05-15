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
