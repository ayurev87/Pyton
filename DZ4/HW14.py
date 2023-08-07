# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import Decimal 

num_float = float(input("Введите число: "))
d_round = float(input("Введите точность округления числа в формате 0.00001: "))

def round_number(number, d):
    number_1 = Decimal(f"{number}")
    number_1 = number_1.quantize(Decimal(f"{d}"))
    return number_1

print(round_number(num_float, d_round))