import data_base_init as db


def input_person_info(titles):
    name_list = []
    for i in titles:
        name = input(f'Введите значения для поля "{i}":\t')
        if i.isdigit() == True:
            name = int(name)
        name_list.append(name)
        personal_info = []
        personal_info.append(tuple(name_list))
    return personal_info

def input_select_name(name_list, name_list_en):
    name = ''
    value = ''
    while True:
        name, value = input(f'Введите название({name_list[0]}, {name_list[1]}, {name_list[2]}) и значение колонки для строки, которую(ые) хотите просмотреть: \t').split()
        if name.isdigit() or value.isdigit():
            print('Ошибка ввода, корректное строковое значение.')
        else:
            if name == name_list[0]:
                name = name_list_en[0]
            elif name == name_list[1]:
                name = name_list_en[1]
            elif name == name_list[2]:
                name = name_list_en[2]
        return name, value


def input_delete_name(name_list, name_list_en):
    name = ''
    value = ''
    while True:
        name, value = input(f'Введите название({name_list[0]}, {name_list[1]}, {name_list[2]}) и значение колонки для строки, которую(ые) хотите удалить: \t').split()
        if name.isdigit() or value.isdigit():
            print('Ошибка ввода, корректное строковое значение.')
        else:
            if name == name_list[0]:
                name = name_list_en[0]
            elif name == name_list[1]:
                name = name_list_en[1]
            elif name == name_list[2]:
                name = name_list_en[2]
        return name, value
    
    
def input_select_id():
    number_id = 0
    while True:
        number_id = input('Введите значение id для строки, которую хотите просмотреть: \t')
        if number_id.isdigit():
            number_id = int(number_id)
            return number_id
        else:
            print('Ошибка ввода, ожидается целое число.')


def input_delete_id():
    number_id = 0
    while True:
        number_id = input('Введите значение id для строки, которую хотите удалить: \t')
        if number_id.isdigit():
            number_id = int(number_id)
            return number_id
        else:
            print('Ошибка ввода, ожидается целое число.')


def output_table_to_console():
    count = db.curs.rowcount
    if count == 0:
        print('\n\t\tТАБЛИЦА ПУСТА.')
    else:
        for i in db.curs.execute('SELECT * FROM  personal'):
            print(*i)
        
def is_select(is_true):
    if is_true == True:
        print('Строка(ки) успешно показана!')
    else:
        print('Вывод завершилося неудачей.')
        
        
def is_insert(is_true):
    if is_true == True:
        print('Строка(ки) успешно добавлена!')
    else:
        print('Добавление завершилось неудачей.')
        

def is_deleted(is_true):
    if is_true == True:
        print('Строка(ки) успешно удалена!')
    else:
        print('Удаление завершилось неудачей.')
        
        
def output_the_table():
    while True:
        choice = input('Хотите ли Вы увидеть таблицу,для выбора нажмите y/n (да/нет):\t')
        if choice == 'y':
            output_table_to_console()
            break
        elif choice == 'n':
            break
        else:
            print('Ошибка. Повторите ввод.')
            
            
def menu():
    while True:
        choice = input('''
            Выберите дейстие. Введите:\n
            1 - чтобы просмотреть таблицу
            2 - чтобы показать запись по id запись(си) по значению колонки
            3 - чтобы внести запись
            4 - чтобы удалить запись
            5 - чтобы выйти\n''')
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
            print('Ошибка. Повторите ввод.')
        else:
            break
    return int(choice)
        
        
def exit_program():            
    choice = input('Для выхода нажмите "q":\t')
    if choice == 'q':
        quit()