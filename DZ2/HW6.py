# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input('Введите число n: '))

def sequence_num(number):
    sum = 0
    list = []
    for i in range(1, number + 1):
        result = round((1 + 1 / i) ** i, 2)
        list.append(result)
    return list


def sum_num(list):
    sum = 0
    for i in range(len(list)):
        sum += float(list[i])
    return sum


sequence_result = sequence_num(num)
sum = sum_num(sequence_result)
print('Последовательность: ', end= '')
print(*sequence_result, sep= ', ')
print(f'Сумма всех чисел приведенной последовательности равна {sum}')