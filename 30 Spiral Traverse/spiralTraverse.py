def spiralTraverse(array):
    starting_row = 0
    ending_row = len(array) - 1
    starting_column = 0
    ending_column = len(array[0]) - 1

    result = []
    while starting_row <= ending_row and starting_column <= ending_column:
        # printing TOP ROW
        for column in range(starting_column, ending_column + 1):
            result.append(array[starting_row][column])

        # printing RIGHT COLUMN
        for row in range(starting_row + 1, ending_row + 1):
            result.append(array[row][ending_column])

        if starting_row == ending_row:
            break
            
        # printing BOTTOM ROW (reversed)
        for column in reversed(range(starting_column, ending_column)):
            result.append(array[ending_row][column])

        if starting_column == ending_column:
            break

        # printing LEFT COLUMN (reversed)
        for row in reversed(range(starting_row + 1, ending_row)):
            result.append(array[row][starting_column])

        starting_row += 1
        starting_column += 1
        ending_row -= 1
        ending_column -= 1
            

    return result


array = [
    [ 1,  2,  3,  4],
    [12, 13, 14,  5],
    [11, 16, 15,  6],
    [10,  9,  8,  7]
]

print(spiralTraverse(array))




