def bubbleSort(array):
    isSorted = False
    counter = 0

    while not isSorted:
        isSorted = True
        for index in range(0, len(array) - 1 - counter):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                isSorted = False
        counter += 1
    return array