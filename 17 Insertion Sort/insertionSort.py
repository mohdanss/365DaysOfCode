def insertionSort(array):
    for i_index in range(1, len(array)):
        j_index = i_index
        while j_index > 0 and array[j_index] < array[j_index - 1]:
            array[j_index], array[j_index - 1] = array[j_index - 1], array[j_index]
            j_index -= 1
    return array