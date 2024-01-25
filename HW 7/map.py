'''print_operation_table
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента
 функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
у операции умножения.
Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
Пример
На входе:
print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:
1 2 3
2 4 6 
3 6 9'''


# def print_operation_table(operation, num_rows=9, num_columns=9): 
#     res = []
#     if num_rows <2: 
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1, num_rows+1):
#             for j in range(1, num_columns+1):
#                 res.append(operation(i,j))
#                 # вариант вывода 1
#             print(*res)
#             res = []
# #                 # вариант вывода 2
# # #     for i in range(0, len(res), num_columns):
# # #         print(*res[0 + i: num_columns + i])
# print_operation_table(lambda x, y: x * y, 10, 10)

'''Винни Пух
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько 
просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите 
Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше 
одной!.
На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
На выходе:
Парам пам-пам
'''
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
list_1 = stroka.split(" ")
glasn = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я', 'ё']
res = list()
def puh():
    if len(list_1) == 1: return "Количество фраз должно быть больше одной!" 
    else:
        for i in list_1:
            res.append(len([j for j in i if j in glasn]))
        #     print([j for j in i if j in ""])
        # print(res)
            # count = 0
            # for j in i:
            #     if j in glasn: 
            #         count += 1
            # res.append(count)
            # 1 вариант сравнения
        # if len(res) == res.count(res[0]):
            # 2 вариант сравнения
        if len(set(res)) == 1:
            return "Парам пам-пам"
        else:
            return "Пам парам"            
print(puh()) 

'''
Атрибуты
'''
# print(__name__)
# if __name__ != '__main__':
#     # print(111)
# a = 3.4

# print(dir(a))

# print(a.__class__)
# print(a.__ceil__())
# print(a.__eq__(3.4))