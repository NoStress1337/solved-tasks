'''
На вход программе подаются два натуральных числа nn и mm — количество строк и
столбцов в матрице. Создайте матрицу mult размером n×m и заполните её таблицей
умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа n и m — количество строк
и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа 
ровно 33 символа (для этого используйте строковый метод ljust()).
'''
def multiplication_table(n : int, m : int) -> list:
    matrix = []
    for i in range(n):
        temp = [i * j for j in range(m)]
        matrix.append(temp)
    return matrix

def print_matrix(matrix_list : list) -> None:
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            print(str(matrix_list[i][j]).ljust(3), end='')
        print()

matrix = multiplication_table(int(input()), int(input()))
print_matrix(matrix)