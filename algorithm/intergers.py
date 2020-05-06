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
