'''
Напишите программу, которая считывает элементы матрицы один за другим,
выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу,
но уже поменяв местами строки со столбцами: первая строка выводится как
первый столбец, и так далее.

Формат входных данных
На вход программе подаются два числа nn и mm — количество строк и столбцов
в матрице, далее идут  n×m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, за ней пустую строку,
и ту же матрицу, но поменяв местами строки со столбцами. Элементы матрицы
разделять одним пробелом.
'''
def input_matrix(n : int, m : int) -> list:
    matrix = []
    for i in range(n):
        temp = [input() for j in range(m)]
        matrix.append(temp)
    return matrix

def print_matrix(matrix_list : list) -> None:
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            print(matrix_list[i][j], end=' ')
        print()

def print_transpose_matrix(matrix_list : list) -> None:
    for i in range(len(matrix_list[0])):
        for j in range(len(matrix_list)):
            print(matrix_list[j][i], end=' ')
        print()

matrix = input_matrix(int(input()), int(input()))

print_matrix(matrix)
print()
print_transpose_matrix(matrix)