import data_base_init as db
import model as m
import view as v


def run_application():
    # personal_info = [("Иван", "Иванов", "Генеральным директор", 250000, 80000)]
    
    personal_titles = db.title_list     # column names in russian
    personal_titles_en = db.title_list_en      # column names in english
    
    # MAIN
    while True:
            # OUTPUT THE TABLE INTO CONSOLE
        while True:
            choice = input('Хотите ли Вы увидеть таблицу,для выбора нажмите y/n (да/нет):\t')
            if choice == 'y':
                v.output_table_to_console()
                break
            elif choice == 'n':
                break
            else:
                print('Ошибка. Повторите ввод.')
        menu_choice = v.menu()
        if menu_choice == 1:
            v.output_table_to_console()
        elif menu_choice == 2:
            while True:
                choice = input('Вы хотите просмотреть конкретную запись по id (нажать 1) или несколько по кому-либо значению(нажать 2)?:\t')
                if choice != '1' and choice != '2':
                    print('Ошибка. Повторите ввод.')
                elif choice == '1':
                    number = v.input_select_id()
                    is_true = m.select_row_by_id(number)
                    v.is_select(is_true)
                    v.exit_program()
                    break
                elif choice == '2':
                    name, value = v.input_select_name(personal_titles, personal_titles_en)
                    is_true = m.select_row_by_somename_str(name, value)
                    v.is_select(is_true)
                    v.exit_program()
                    break
        elif menu_choice == 3:
            personal_info = v.input_person_info(personal_titles)
            is_true = m.insert_row(personal_info)
            v.is_insert(is_true)
        elif menu_choice == 4:
            while True:
                choice = input('Вы хотите удалить конкретную запись по id (нажать 1) или несколько по кому-либо значению(нажать 2)?:\t')
                if choice != '1' and choice != '2':
                    print('Ошибка. Повторите ввод.')
                elif choice == '1':
                    number = v.input_delete_id()
                    is_true = m.delete_row_by_id(number)
                    v.is_deleted(is_true)
                    v.exit_program()
                    break
                elif choice == '2':
                    name, value = v.input_delete_name(personal_titles, personal_titles_en)
                    is_true = m.delete_row_by_somename_str(name, value)
                    v.is_deleted(is_true)
                    v.exit_program()
                    break
        elif menu_choice == 5:
            print('Удачи! Ждем еще)))')
            break