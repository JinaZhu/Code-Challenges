# bubble sort

notSorted = [5, 2, 1, 9, 3, 8, 7, 4, 6]


def bubblesort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


print(bubblesort(notSorted))
