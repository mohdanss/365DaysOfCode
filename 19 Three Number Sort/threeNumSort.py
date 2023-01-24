def threeNumberSort(array, order):
    index = 0
    for i in range(2):
        num = order[i]
        for j in range(len(array)):
            if array[j] == num and j >= index:
                swap(index, j, array)
    return array

def swap(a, b, array):
    array[a], array[b] = array[b], array[a]


