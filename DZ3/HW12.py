#  Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

def input_list():
    user_list = input('Введите несколько вещественных чисел через пробел: ').split(' ')
    return user_list


def find_difference(user_list):
    current_value = 0.0
    min_value = float(user_list[0]) % 1
    max_value = float(user_list[0]) % 1
    error_correction = 0.0000000000000001
    for i in user_list:
        current_value = float(i) % 1
        if current_value != 0:
            if current_value > max_value:
                max_value = current_value
            elif current_value < min_value:
                min_value = current_value
        difference = max_value - min_value + error_correction
        difference = round(difference, 14)
    return difference


user_lst = input_list()
result = find_difference(user_lst)
print(f'Разница между максимальным и миниманым дробным значением состовляет {result}')