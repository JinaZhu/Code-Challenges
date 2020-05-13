# You have an endless supply of dimes and pennies. How many different amounts of total change can you make using exactly num_coins number coins?
# For example, when num_coins = 3, you can create 4 different kinds of change:


def num_coins(coins):
    # create a set to ensure there is no repeats
    result = set()
    for dimes in range(coins+1):
        pennies = coins - dimes
        result.add((dimes * 10) + pennies)

    return len(result)


print('num_coins', num_coins(1000))

# find the area of a polygon for a given n.


def polygon_area(num):
    # keep track of the total number of squares
    count = 1
    # keep track of how many to add up from each level
    add_on = 4

    for i in range(1, num):
        count += add_on
        add_on += 4

    return count


print('polygon_area', polygon_area(3))
print('polygon_area', polygon_area(100))

# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.


def int_to_roman(int):
    # keep track of symbols
    roman_dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    result = ""

    while int != 0:
        # looping through the keys, check if int is greater than or equal to int and if so, add value to str and subtract int by key
        for key in roman_dict:
            if int >= key:
                result += roman_dict[key]
                int -= key
                break

    return result


print('int_to_roman', int_to_roman(1994))
print('int_to_roman', int_to_roman(4))

# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


def roman_to_int(roman_str):
    roman_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    position_tracker = 0
    counter = 0

    while position_tracker != len(roman_str):
        if position_tracker == len(roman_str) - 1:
            counter += roman_dict[roman_str[position_tracker]]
            position_tracker += 1
            break
        two_char = roman_str[position_tracker] + roman_str[position_tracker+1]
        if two_char in roman_dict.keys():
            counter += roman_dict[two_char]
            position_tracker += 2
        else:
            counter += roman_dict[roman_str[position_tracker]]
            position_tracker += 1

    return counter


print('roman_to_int', roman_to_int('LVIII'))
print('roman_to_int', roman_to_int("MCMXCIV"))


# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.


def single_digit(num):
    # if num is less than 9, return the num
    if num <= 9:
        return num
    # as long as the num is greater than 9, convert num into a list of strings, then convert strings into int and sum list, reassign num to be the sum
    while num > 9:
        int_to_lst = list(str(num))
        int_lst = list(map(int, int_to_lst))
        all_sum = sum(int_lst)

        num = all_sum

    return num


print('single_digit', single_digit(32))
print('single_digit', single_digit(38))

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# actual function


def pascal_tri(num):
    if num == 0:
        return []
    # store the first line which will always be [1] so there is something to pass in to the helper function
    result = [[1]]
    # as long as this length of result is less than or equal to num, call the helper function to get the next line
    while len(result) <= num:
        new_line = sum_line(result[-1])
        result.append(new_line)

    return result

# helper function


def sum_line(previous_line):
    new_line = [1]
    # loop to find the sum of the current item and previous item
    for i in range(1, len(previous_line)):
        sum = previous_line[i] + previous_line[i - 1]
        new_line.append(sum)

    new_line.append(1)
    return new_line


print('pascal_tri', pascal_tri(5))

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.


def find_max_avg(lst, length):
    tracker = sum(lst[:length])
    largest_avg = tracker / length

    for i in range(0, len(lst) - length):
        tracker -= lst[i]
        tracker += lst[i+length]
        largest_avg = max(largest_avg, tracker/length)

    return largest_avg


print('find_max_avg', find_max_avg([1, 12, -5, -6, 50, 3], 4))
