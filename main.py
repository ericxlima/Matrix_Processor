def create_matrix(size: str, matrix_name='') -> tuple:
    m, n = list(map(int, input(size).split(' ')))
    if matrix_name:
        print(matrix_name)
    matrix = [list(map(float, input().split(' '))) for _ in range(m)]
    return m, n, matrix


def print_matrix(matrix: list):
    print('The result is:')
    for line in matrix:
        print(*line)


def sum_matrices():
    m1, n1, matrix1 = create_matrix('Enter size of first matrix: ', 'Enter first matrix:')
    m2, n2, matrix2 = create_matrix('Enter size of second matrix: ', 'Enter second matrix:')
    if (m1, n1) == (m2, n2):
        size = {'line': m1, 'column': n1}
        new_matrix = []
        for line in range(size['line']):
            new_matrix.append([])
            for column in range(size['column']):
                new_matrix[line].append(matrix1[line][column] + matrix2[line][column])
        print_matrix(new_matrix)
    else:
        print('The operation cannot be performed.')


def multiply_by_constant():
    _, _, matrix = create_matrix('Enter size of matrix: ')
    constant = int(input('Enter constant: '))
    new_matrix = []
    for line in matrix:
        new_matrix.append([constant * num for num in line])
    print_matrix(new_matrix)


def multiply_matrices():
    m1, n1, matrix1 = create_matrix('Enter size of first matrix: ', 'Enter first matrix:')
    m2, n2, matrix2 = create_matrix('Enter size of second matrix: ', 'Enter second matrix:')
    if n1 == m2:
        new_matrix = []
        for line in range(m1):
            matrix1_line = matrix1[line]
            new_matrix.append([])
            for column in range(n2):
                matrix2_column = [line[column] for line in matrix2]
                new_matrix[line].append(sum([matrix1_line[i] * matrix2_column[i] for i in range(len(matrix1_line))]))
        print_matrix(new_matrix)


def transpose_matrix():
    transp_menu = input('\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: ')
    m, n, matrix = create_matrix('Enter matrix size: ')
    new_matrix = []
    if transp_menu == '1':
        new_matrix = [list(t) for t in zip(*matrix)]
    elif transp_menu == '2':
        for index, _ in enumerate(matrix, start=1):
            new_matrix.append([x[-index] for x in reversed(matrix)])
    elif transp_menu == '3':
        new_matrix = [reversed(line) for line in matrix]
    elif transp_menu == '4':
        new_matrix = reversed(matrix)
    print_matrix(new_matrix)


def matrix_determination():

    def matrix_get_minor(i, j, matrix):
        return [row[:j] + row[j + 1:] for row in matrix[:i] + matrix[i + 1:]]

    def matrix_get_determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            determinant = 0
            for x in range(len(matrix)):
                determinant += matrix[x][0] * ((-1) ** x) * matrix_get_determinant(matrix_get_minor(x, 0, matrix))
            return determinant

    m, n, mat = create_matrix('Enter matrix size: ')
    det = matrix_get_determinant(mat)
    print(f"The result is: \n{det}")


def inverse_matrix():
    pass


def main():
    menu = None
    while menu != '0':
        if menu == '1':
            sum_matrices()
        if menu == '2':
            multiply_by_constant()
        if menu == '3':
            multiply_matrices()
        if menu == '4':
            transpose_matrix()
        if menu == '5':
            matrix_determination()
        if menu == '6':
            inverse_matrix()
        menu = input('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose '
                     'matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit\nYour choice: ')


if __name__ == '__main__':
    main()
