# Charlie Juarez
# Restrictions: Integer matrices, defined matrices
import time
import random

class Matrix(object):
    row = 0
    column = 0
    matrix = []

    def __init__(self, row, column, matrix):
        self.row = row
        self.column = column
        self.matrix = matrix

    # Function to print the values inside the matrix
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
    print('The multiplication of the matrices took '+str(elapsed_time)+' seconds.')

# Function to create a matrix
def create_matrix():
    matrix = []
    row = int(input('Provide the number of rows in the matrix: '))
    column = int(input('Provide the number of columns in the matrix: '))

    # Input the values into the matrix
    for num1 in range(row):
        temp_arr = []
        for num2 in range(column):
            temp_arr.append(random.randint(99999999999999, 99999999999999999))
        matrix.append(temp_arr)

    matrix = Matrix(row, column, matrix)
    print('With your response you have created the following matrix:')
    matrix.print_matrix()
    return matrix

# Function to multiply matrices
def multiply_matrices(matrix1, matrix2):
    matrix = []

    # Create an empty matrix with the appropriate dimensions
    for num1 in range(matrix1.row):
        temp_arr = []
        for num2 in range(matrix2.column):
            temp_arr.append(0)
        matrix.append(temp_arr)

    # Fill in the values of the product of matrices
    # Iterate through rows of matrix1
    for i in range(matrix1.row):
        # Iterate through columns of matrix2
        for j in range(matrix2.column):
            # Iterate through rows of matrix2
            for k in range(matrix2.row):
                matrix[i][j] += matrix1.matrix[i][k] * matrix2.matrix[k][j]
    
    matrix3 = Matrix(matrix1.row, matrix2.column, matrix)
    print('The multiplication of the matrices have yielded the following matrix:')
    matrix3.print_matrix()
    return matrix3


if __name__ == "__main__":
    main()
