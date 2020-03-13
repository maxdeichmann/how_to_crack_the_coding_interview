def rotate_matrix(matrix):
    columns = []
    for n in range(len(matrix[0])):
        column = []
        for m in range(len(matrix)):
            column.append(matrix[m][n])
        column.reverse()
        columns.append(column)
    return columns



matrix =    [[1,2,3],
            [4,5,6],
            [7,8,9]]




print(rotate_matrix(matrix))


# 741
# 852
# 963