def selectionSort(array):
    for i in range(len(array) - 1):
        currentMin = i
        for j in range(currentMin + 1, len(array)):
            if array[currentMin] > array[j]:
                currentMin = j
        swap(i, currentMin, array)
    
    return array

def swap(a, b, array):
    array[a], array[b] = array[b], array[a]