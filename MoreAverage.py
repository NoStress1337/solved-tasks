'''
Напишите программу, которая выводит количество элементов квадратной матрицы в
каждой строке, больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов
в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести n чисел — для каждой строки количество элементов матрицы,
больших среднего арифметического элементов данной строки.
'''
def matrix(n : int) -> list:
    matrix = [input().split() for _ in range(n)]
    return matrix

def count_more_average(matrix : list) -> list:
    count_list = []
    for i in range(len(matrix)):
        average, count = 0, 0
        for j in range(len(matrix)):
            average += int(matrix[i][j])
        average = average / len(matrix)
        for g in range(len(matrix)):
            if int(matrix[i][g]) > average:
                count += 1
        count_list.append(count)
    return count_list        

print(*count_more_average(matrix(int(input()))), sep="\n")