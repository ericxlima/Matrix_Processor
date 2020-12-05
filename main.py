def create_matrix(m: int) -> list:
    matrix = [list(map(float, input().split(' '))) for _ in range(m)]
    return matrix


def sum_matrices():
    try:
        m1, n1 = list(map(int, input('Enter size of first matrix: ').split(' ')))
        print('Enter first matrix:')
        matrix1 = create_matrix(m1)
        m2, n2 = list(map(int, input('Enter size of second matrix: ').split(' ')))
        print('Enter second matrix:')
        matrix2 = create_matrix(m2)

        if (m1, n1) == (m2, n2):
            size = {'line': m1, 'column': n1}
            print('The result is:')
            new_matrix = []
            for line in range(size['line']):
                new_matrix.append([])
                for column in range(size['column']):
                    new_matrix[line].append(matrix1[line][column] + matrix2[line][column])
            for line in new_matrix:
                print(' '.join(list(map(str, line))))
        else:
            raise EOFError
    except:
        print('The operation cannot be performed.')


def multiply_by_constant():
    m, n = list(map(int, input('Enter size of matrix: ').split(' ')))
    matrix1 = create_matrix(m)
    constant = int(input('Enter constant: '))
    new_matrix = []
    for line in matrix1:
        new_matrix.append([constant * column for column in line])
    print('The result is:')
    for line in new_matrix:
        print(' '.join(list(map(str, line))))


def multiply_matrices():
    m1, n1 = list(map(int, input('Enter size of first matrix: ').split(' ')))
    print('Enter first matrix:')
    matrix1 = create_matrix(m1)
    m2, n2 = list(map(int, input('Enter size of second matrix: ').split(' ')))
    print('Enter second matrix:')
    matrix2 = create_matrix(m2)
    if n1 == m2:
        print('The result is:')
        new_matrix = []
        for line in range(m1):
            matrix1_line = matrix1[line]
            new_matrix.append([])
            for column in range(n2):
                matrix2_column = [line[column] for line in matrix2]
                new_matrix[line].append(sum([matrix1_line[i] * matrix2_column[i] for i in range(len(matrix1_line))]))
        for line in new_matrix:
            print(' '.join(list(map(str, line))))


def main():
    menu = None
    while menu != '0':
        if menu == '1':
            sum_matrices()
        if menu == '2':
            multiply_by_constant()
        if menu == '3':
            multiply_matrices()
        menu = input('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit\nYour choice: ')


if __name__ == '__main__':
    main()
