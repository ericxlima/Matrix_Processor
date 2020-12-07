def create_matrix(m: int) -> list:
    matrix = [list(map(float, input().split(' '))) for _ in range(m)]
    return matrix


def print_matrix(matrix):
    print('The result is:')
    for line in matrix:
        print(' '.join(list(map(str, line))))


def sub_matrices():
    try:
        m1, n1 = list(map(int, input('\nEnter size of first matrix: ').split(' ')))
        print('Enter first matrix:')
        matrix1 = create_matrix(m1)
        m2, n2 = list(map(int, input('Enter size of second matrix: ').split(' ')))
        print('Enter second matrix:')
        matrix2 = create_matrix(m2)

        if (m1, n1) == (m2, n2):
            size = {'line': m1, 'column': n1}
            new_matrix = []
            for line in range(size['line']):
                new_matrix.append([])
                for column in range(size['column']):
                    new_matrix[line].append(matrix1[line][column] - matrix2[line][column])
            print_matrix(new_matrix)
        else:
            raise EOFError
    except:
        print('The operation cannot be performed.')


def sum_matrices():
    try:
        m1, n1 = list(map(int, input('\nEnter size of first matrix: ').split(' ')))
        print('Enter first matrix:')
        matrix1 = create_matrix(m1)
        m2, n2 = list(map(int, input('Enter size of second matrix: ').split(' ')))
        print('Enter second matrix:')
        matrix2 = create_matrix(m2)

        if (m1, n1) == (m2, n2):
            size = {'line': m1, 'column': n1}
            new_matrix = []
            for line in range(size['line']):
                new_matrix.append([])
                for column in range(size['column']):
                    new_matrix[line].append(matrix1[line][column] + matrix2[line][column])
            print_matrix(new_matrix)
        else:
            raise EOFError
    except:
        print('The operation cannot be performed.')


def multiply_by_constant():
    m, n = list(map(int, input('\nEnter size of matrix: ').split(' ')))
    matrix1 = create_matrix(m)
    constant = int(input('Enter constant: '))
    new_matrix = []
    for line in matrix1:
        new_matrix.append([constant * column for column in line])
    print_matrix(new_matrix)


def multiply_matrices():
    m1, n1 = list(map(int, input('\nEnter size of first matrix: ').split(' ')))
    print('Enter first matrix:')
    matrix1 = create_matrix(m1)
    m2, n2 = list(map(int, input('Enter size of second matrix: ').split(' ')))
    print('Enter second matrix:')
    matrix2 = create_matrix(m2)
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
    menu = input('\n1. Main diagonal (REAL)\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: ')
    m, n = list(map(int, input('Enter matrix size: ').split(' ')))
    matrix = create_matrix(m)
    new_matrix = []
    if menu == '1':
        for t in zip(*matrix):
            new_matrix.append(list(t))
    elif menu == '2':
        for index, _ in enumerate(matrix, start=1):
            new_matrix.append([x[-index] for x in reversed(matrix)])
    elif menu == '3':
        for line in matrix:
            new_matrix.append(reversed(line))
    elif menu == '4':
        new_matrix = reversed(matrix)
    print_matrix(new_matrix)


def main():
    menu = None
    while menu != '0':
        if menu == '1':
            sum_matrices()
        if menu == '2':
            sub_matrices()
        if menu == '3':
            multiply_by_constant()
        if menu == '4':
            multiply_matrices()
        if menu == '5':
            transpose_matrix()
        menu = input('1. Add matrices\n2. Subtraction matrices\n3. Multiply matrix by a constant\n4. Multiply '
                     'matrices\n5. Transpose matrix\n0. Exit\nYour choice: ')


if __name__ == '__main__':
    main()
