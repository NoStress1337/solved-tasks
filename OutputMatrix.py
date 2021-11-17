'''
Напишите программу, которая сначала считывает элементы матрицы один за другим,
затем выводит их в виде матрицы.

Формат входных данных
На вход программе подаются два числа n и m — количество строк и столбцов в 
матрице, далее идут n×m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
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

print_matrix(input_matrix(int(input()), int(input())))