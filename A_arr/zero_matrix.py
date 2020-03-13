def zero_matrix(matrix):
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if matrix[m][n] is 0:
                matrix[m] = [0 for _ in range(len(matrix[m]))]
                for i in range(len(matrix)):
                    matrix[i][n] = 0
                return matrix






matrix =    [[1,2,3],
            [4,0,6],
            [7,8,9]]



print(zero_matrix(matrix))