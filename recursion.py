# write a function that return the index of a given item in a list recursively


def finder(item, lst, counter=0):
    # if the list is empty, return false
    if (len(lst) == 0):
        return False
    # set counter to be the length of the items
    counter = len(lst)
    # while the list isnt empty
    while(lst):
        # decrease count
        counter -= 1
        # pop and store the last item from list
        lastItem = lst.pop()
        # if last item is equal to given item
        if lastItem == item:
            # return the counter
            return counter
        # if not, call finder and pass in a new list and updated counter
        return finder(item, lst, counter)
    # once the loop end, and item is not found, return false
    return False


lst = ["hey", "there", "you"]
print('False', finder('I', lst))
lst2 = [1, 2, 3, 5, 6, 7, 8, 9, 0, 3, 2, 5, 6]
print('5', finder(7, lst2))

# Given a number N return the index value of the Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

# iterate solution


def iterate_fibonacci(num):
    # create a list to store all the num
    lst = [0, 1]
    # loop through starting with 2 to given number +1
    for index in range(2, num+1):
        # append the sum of the last 2 numbers in the list
        lst.append(lst[index-2] + lst[index - 1])
    # return the last item
    return lst[-1]


print('55', iterate_fibonacci(10))

# recursive solution


def recursive_fibonacci(num):
    if num < 2:
        return num

    return (recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2))


print('55', recursive_fibonacci(10))

# cache solutions:


def cache_fibonacci(num, cache={}):
    # if num in cache dict, return the value
    if num in cache:
        return cache[num]
    # else, if num is less than 2, return num or add the sum to the dict
    else:
        if num < 2:
            return num
        else:
            cache[num] = cache_fibonacci(
                num-1, cache) + cache_fibonacci(num-2, cache)
            return cache[num]


print('55', cache_fibonacci(10))
