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


print(polygon_area(3))
print(polygon_area(100))
