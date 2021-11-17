'''
Напишите программу, которая вычисляет сумму элементов: 
верхней четверти; 
правой четверти; 
нижней четверти; 
левой четверти.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и
столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
def matrix(n : int) -> list:
    matrix = []
    for _ in range(n):
        row = [int(i) for i in input().split()]
        matrix.append(row)
    return matrix

def sum_in_area(matrix : list) -> int:
    sum_up, sum_left, sum_right, sum_down = 0, 0, 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > j:
                if i < len(matrix) - 1 - j:
                    sum_left += matrix[i][j]
                elif i > len(matrix) - 1 - j:
                    sum_down += matrix[i][j]
            if i < j:
                if i < len(matrix) - 1 - j:
                    sum_up += matrix[i][j]
                elif i > len(matrix) - 1 - j:
                    sum_right += matrix[i][j]
    return sum_up, sum_right, sum_down, sum_left

sums = sum_in_area(matrix(int(input())))

print("Верхняя четверть:", sums[1])
print("Правая четверть:", sums[2])
print("Нижняя четверть:", sums[3])
print("Левая четверть:", sums[4])