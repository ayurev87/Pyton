# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

def find_product(number):
    factorial = 1
    list = []
    for n in range(1, number + 1):
        factorial *= n
        list.append(factorial)
    return list


num = int(input('Введите любое целое число: '))
result = find_product(num)
print(f'Факториалом числел от 1 до {num} являются ', end= '' )
print(result, end= '')