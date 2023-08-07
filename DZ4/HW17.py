# ;  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# ; in
# ; 9
# ; 5
# ; 3

# ; out in the file
# ; 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# ; 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# ; 4*x^2 - 4 = 0

import random


def write_to_file_ratois(degree):
    a = random.randint(0, 11)
    b = random.randint(0, 11)
    c = random.randint(0, 11)
    with open('multiple_task034.txt', 'w') as f:
        f.write(f'{a}x^{degree} + {b}x + {c}')
    

num = int(input('Введите натуральную степнь k: '))
write_to_file_ratois(num)