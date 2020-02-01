# Charlie Juarez
# Restrictions: Integer matrices, defined matrices
import time

class Matrix(object):
    row = 0
    column = 0
    matrix = []

    def __init__(self, row, column, matrix):
        self.row = row
        self.column = column
        self.matrix = matrix

    def print_matrix(self):
        for num1 in range(self.row):
            for num2 in range(self.column):
                print(self.matrix[num1][num2], end=' ')
            print()


def main():
    matrix1 = create_matrix()
    matrix2 = create_matrix()
    start = time.time()
    matrix3 = multiply_matrices(matrix1, matrix2)
    end = time.time()
    elapsed_time = end - start
    print(elapsed_time)


def create_matrix():
    matrix = []
    row = int(input('Provide the number of rows in the matrix: '))
    column = int(input('Provide the number of columns in the matrix: '))
    for num1 in range(row):
        temp_arr = []
        for num2 in range(column):
            temp_arr.append(int(input('Provide a number to input into the matrix: ')))
        matrix.append(temp_arr)
    matrix = Matrix(row, column, matrix)
    print('With your response you have created the following matrix:')
    matrix.print_matrix()
    return matrix


def multiply_matrices(matrix1, matrix2):
    matrix3 = []
    row = matrix1.row
    column = matrix2.column
    for num1 in range(row):
        temp_arr = []
        result = 0
        for num2 in range(column):
            temp1 = matrix1.matrix[num1][num2]
            temp2 = matrix2.matrix[num2][num1]
            result += temp1*temp2
            temp_arr.append(result)
        matrix3.append(temp_arr)
    matrix3 = Matrix(row, column, matrix3)
    matrix3.print_matrix()
    return matrix3


if __name__ == "__main__":
    main()
