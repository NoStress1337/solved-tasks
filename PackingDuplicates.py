'''
На вход программе подается строка текста, содержащая символы. Напишите программу,
которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.
'''
def packing(split_list : list) -> list:
    packed_list = [[split_list[0]]]
    for i in range(1, len(split_list)):
        if split_list[i] == split_list[i - 1]:
            packed_list[-1].append(split_list[i])
        else:
            packed_list.append([split_list[i]])
    return packed_list

print(packing(input().split()))