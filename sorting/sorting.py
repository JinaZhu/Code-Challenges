notSorted = [5, 2, 1, 9, 3, 8, 7, 4, 6]

# bubble sort


def bubblesort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


print(bubblesort(notSorted))

# merge sort


def merge_sort(lst):
    # if the list is 1, return list
    if len(lst) < 2:
        return lst

    middle = len(lst)//2  # middle point
    lst1 = merge_sort(lst[:middle])  # first half pass in merge
    lst2 = merge_sort(lst[middle:])  # second half pass in merge

    return make_merge(lst1, lst2)


def make_merge(lst1, lst2):
    result = []

    # as long as lst1 or lst2 is not empty
    while lst1 or lst2:
        if lst1 == []:
            result.append(lst2.pop(0))
        elif lst2 == []:
            result.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))

    return result


print(merge_sort(notSorted))

# quick sort


def quick_sort(lst):
    if len(lst) < 2:
        return lst

    middle = len(lst)//2
    pivot = lst[middle]

    low = []
    high = []
    equal = []

    for item in lst:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        else:
            equal.append(item)

    return quick_sort(low) + equal + quick_sort(high)


print(quick_sort(notSorted))
