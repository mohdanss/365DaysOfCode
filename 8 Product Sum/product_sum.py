def productSum(array, depth = 1):
    print(array)
    sum = 0
    for element in array:
        if type(element) == int:
            sum += element
        else:
            sum += productSum(element, depth + 1)
        print(sum)
    return sum * depth