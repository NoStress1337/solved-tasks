'''
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа 
n и m — количество строк и столбцов в матрице, затем элементы матрицы 
построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.
'''
def matrix(n : int, m : int) -> list:
    matrix = []
    for _ in range(n):
        row = [int(i) for i in input().split()]
        matrix.append(row)
    return matrix

def cl_swap(cl : list, matrix : int) ->  list:
    for i in range(len(matrix)):
        matrix[i][cl[0]], matrix[i][cl[1]] = matrix[i][cl[1]], matrix[i][cl[0]]
    return matrix

def print_matrix(matrix_list : list) -> None:
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            print(str(matrix_list[i][j]).ljust(3), end='')
        print()

matrix = matrix(int(input()), int(input()))

print_matrix(cl_swap([int(i) for i in input().split()], matrix))

