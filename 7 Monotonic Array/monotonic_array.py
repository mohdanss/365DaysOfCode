def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True

    for iterator in range(1, len(array)):
        if array[iterator] > array[iterator - 1]:
            isNonDecreasing = False
        if array[iterator] < array[iterator - 1]:
            isNonIncreasing = False
    return isNonIncreasing or isNonDecreasing