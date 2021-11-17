'''
Напишите программу, которая выводит след заданной квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и
столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — след заданной матрицы.
'''
def matrix(n : int) -> list:
    matrix = [input().split() for _ in range(n)]
    return matrix

def matrix_trace(matrix : list) -> int:
    matrix_trace = 0
    for i in range(len(matrix)):
        matrix_trace += int(matrix[i][i])
    return matrix_trace

print(matrix_trace(matrix(int(input()))))