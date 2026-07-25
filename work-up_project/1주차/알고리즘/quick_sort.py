import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = []
    greater = []
    equal = []

    for item in arr:
        if item > pivot:
            greater.append(item)
        elif item < pivot:
            less.append(item)
        else:
            equal.append(item)

    # less, equal, greater
    return quick_sort(less) + equal + quick_sort(greater)
