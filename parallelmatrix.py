# Charlie Juarez
# Restrictions: Integer matrices, defined matrices
import time
import random
import pymp

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
    print('Elapsed time for normal matrix multiply is: '+str(elapsed_time)+' seconds.')
    start = time.time()
    parallel_matrix(matrix1, matrix2, 1)
    end = time.time()
    elapsed_time = end - start
    print('Elapsed time for pymp matrix multiply with 1 thread is: '+str(elapsed_time)+' seconds.')
    start = time.time()
    parallel_matrix(matrix1, matrix2, 2)
    end = time.time()
    elapsed_time = end - start
    print('Elapsed time for pymp matrix multiply with 2 threads is: '+str(elapsed_time)+' seconds.')
    start = time.time()
    parallel_matrix(matrix1, matrix2, 4)
    end = time.time()
    elapsed_time = end - start
    print('Elapsed time for pymp matrix multiply with 4 threads is: '+str(elapsed_time)+' seconds.')
    start = time.time()
    parallel_matrix(matrix1, matrix2, 8)
    end = time.time()
    elapsed_time = end - start
    print('Elapsed time for pymp matrix multiply with 8 threads is: '+str(elapsed_time)+' seconds.')

# Function to create a matrix
def create_matrix():
    matrix = []
    row = int(input('Provide the number of rows in the matrix: '))
    column = int(input('Provide the number of columns in the matrix: '))

    # Input the values into the matrix
    for num1 in range(row):
        temp_arr = []
        for num2 in range(column):
            #temp_arr.append(int(input('Provide a number to input into the matrix: ')))
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

# Function to multiply matrices using pymp
def parallel_matrix(matrix1, matrix2, threadnum):
    matrix = pymp.shared.array((matrix1.row, matrix2.column), dtype='float64')

    # Fill in the values of the product of matrices
    with pymp.Parallel(threadnum) as p:
        # Iterate through rows of matrix1
        for i in p.range(matrix1.row):
            # Iterate through columns of matrix2
            for j in range(matrix2.column):
                # Iterate through rows of matrix2
                for k in range(matrix2.row):
                    matrix[i][j] += matrix1.matrix[i][k] * matrix2.matrix[k][j]
    
    matrix = Matrix(matrix1.row, matrix2.column, matrix)
    print('The multiplication of the matrices with pymp have yielded the following matrix:')
    matrix.print_matrix()
    return matrix


if __name__ == "__main__":
    main()
