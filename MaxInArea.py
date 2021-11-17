'''
Напишите программу, которая выводит максимальный элемент
в заштрихованной области квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов 
в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной 
области квадратной матрицы.
'''
def matrix(n : int) -> list:
    matrix = []
    for _ in range(n):
        row = [int(i) for i in input().split()]
        matrix.append(row)
    return matrix

def max_in_area(matrix : list) -> int:
    max_in_area = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i >= j and matrix[i][j] > max_in_area:
                max_in_area = matrix[i][j]
    return max_in_area

print(max_in_area(matrix(int(input()))))

