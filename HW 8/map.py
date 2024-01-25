'''Дальше пытаешься написать код который
1 показывает эти списки в столбик
2 находит в списке определенную запись и выводит ее, например вводишь фамилию, выходит строка фи  - телефон'''



# list_1 = [['Вершинина Марина', '777'],
#           ['Бурков Евгений', '666'],
#           ['Белозёров Александр', '333'],
#           ['Матвеева Дарина', '555'],
#           ['Горук Татьяна', '111'],
#           ['Голомакина Ольга', '444'],
#           ['Горук Александр', '222']]
# for i in list_1:
    # print(i)
'''
Поиск контакта.
'''

def find_name():
    list_1 = reade()
    name = input('Введите ФИ: ')
    finde = list(filter(lambda x: name in x[0], list_1))
    if len(finde) !=0:
        for i in finde:
            print(i)
            visit()
    else:
        nike = input('ФИ отсутствует в списке контактов. Хотите добавить?\n1 - да\n2 - нет\n: ')
        if nike == '1':
            save_name()
        if nike == '2':
            visit()
        else:
            print('Введена неверная команда.')
            visit()
# find_name()

def visit():
    picachu = input('Хотите продолжить?\n1 - да\n2 - нет\n: ')
    if picachu == "1":
        start()
    elif picachu == "2":
        print('Всего доброго!')
        exit()
    else:
        print('Введена неверная команда.')
        visit()

'''
Удаление данных.
'''
def delite():
    list_1 = reade()
    name = input('Введите ФИ: ')
    len_list_1 = len(list_1)
    rem = []
    for i in list_1:
        if name in i[0]:
            rem.append(i)
    if len(rem) !=0:
        print(*rem, sep='\n')
    if len(rem) == 1:
        list_1.remove(rem[0])
        save(list_1)
        visit()
    elif len(rem) >1:
        num = input('Введите номер телефона: ')
        for j in rem:
            if num == j[1]:
                list_1.remove(j)
                save(list_1)
                visit()
        if len_list_1 == len(list_1):
            print('Такого номера нет.')
            visit()  
    else:
        print('Такого контакта нет.')
        visit() 

    # print(list_1)
# delite()
'''
Редактирование.

'''
def redact():
    list_1 = reade()
    red = input('Кого хотите редактировать?\n: ')
    finde = list(filter(lambda x: red in x[0], list_1))
    if len(finde) !=0:
        for i in finde:
            print(i)
    else:
        print('ФИ отсутствует в списке контактов.')
        visit()
    if len(finde) ==1:
        for i in finde:
            uno = input('Хотите изменить Фи - 1, номер телефона - 2?\n: ')
            if uno == '1':
                    list_1[list_1.index(i)][0] = input('Введите новое ФИ: ')
            elif uno == '2':
                    list_1[list_1.index(i)][1] = input('Введите новый номер телефона: ')
            else:
                print('Введена неверная команда.')
                redact()
    bum = 0
    if len(finde) >1:
        num = input('Введите номер телефона: ')
        for j in finde:
            # print(num, j[1])
            if num == j[1]:
                uno = input('Хотите изменить Фи - 1, номер телефона - 2? ')
                if uno == '1':
                    list_1[list_1.index(j)][0] = input('Введите новое ФИ: ')
                elif uno == '2':
                    list_1[list_1.index(j)][1] = input('Введите новый номер телефона: ')
                else:
                    print('Введена неверная команда.')
                    redact()
            else:
                bum += 1
        if len(finde) == bum:
            print('Такого номера телефона нет.')
    save(list_1)
    visit()

# redact()
    # print(list_1)

'''
Добавление нового контакта.
'''

def save_name():
    list_1 = reade()
    saves = input('Хотите создать новый контакт? Да - 1, нет - 2: ')
    list_2 = []
    if saves == '1':
        name = input('Введите новое ФИ: ')
        list_2.append(name)
        nume = input('Введите новый номер телефона: ')
        list_2.append(nume)
        if len(list(filter(lambda x: list_2 == x, list_1))) > 0: print('Такой контакт и номер уже есть.')
        # print(list_3)
        else:
            list_1.append(list_2)
            save(list_1)
            print('Контакт добавлен.')
            visit() 
    elif saves == "2":
        visit() 
    else:
        print('Введена неверная команда.')
        visit() 
    # print(list_1)

'''
Функция записывания.
'''
def save(list_1):
    with open('Phone Book.txt', 'w', encoding='utf-8') as Phone:
        for i in list_1:
            Phone.write(f'{i[0]},{i[1]}\n')
# save()

'''
Функция считывания. 'r'
'''
def reade():
    spros = []
    with open('Phone Book.txt', 'r+', encoding='utf-8') as Phone:
        for i in Phone.readlines():
            spros.append(i.strip().split(','))
    return spros
# spros = reade()
# print(* spros, sep='\n')

'''
Функция начала Statr.
'''
def start():
    data = input('Что желает мой хозяин?\n1 - Показать список контактов\n2 - Найти контакт\n3 - Добавить новый контак\n4 - Редактировать контакт\n5 - Удалить контакт\n:')
    if data == '1':
        spros = reade()
        print(* spros, sep='\n')
        visit()
    elif data == '2':
        find_name()
    elif data == '3':
        save_name()
    elif data == '4':
        redact()
    elif data == '5':
        delite()
    else:
        print('Введена неверная команда. Попробуйте ещё раз.')
        start()
    # return data
start()