# Time O(n) | Space O(1)
def maxSubsetSumNoAdjacent(array):
    if len(array) < 2:
        return max(array) if len(array) > 0 else 0
    array[1] = max(array[0], array[1])

    for index in range(2, len(array)):
        array[index] = max(array[index - 1], array[index - 2] + array[index])

    return array[-1]

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]))
print(maxSubsetSumNoAdjacent([4, 3, 5, 200, 5, 3]))



