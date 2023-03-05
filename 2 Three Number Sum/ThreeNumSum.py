'''
    Time: O(nlogn) + O(n^2) = O(n^2)
    Space: O(n)
'''
def threeNumberSum(array, targetSum):
    # sort the array O(nlogn)
    array.sort()

    # list to store sums
    sums = []

    for index, num in enumerate(array):
        leftPtr = index + 1
        rightPtr = len(array) - 1
        while leftPtr < rightPtr:
            potentialSum = num + array[leftPtr] + array[rightPtr]

            if potentialSum == targetSum:
                sums.append([num, array[leftPtr], array[rightPtr]])
                leftPtr += 1
                rightPtr -= 1
            elif potentialSum > targetSum:
                rightPtr -= 1
            else:
                leftPtr += 1
    return sums