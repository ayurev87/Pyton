# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


quarter = int(input("Введите номер четверти "))

if quarter == 1:
    print("Диапазон возможных координат: x > 0, y > 0")
if quarter == 3:
    print("Диапазон возможных координат: x < 0, y < 0")
if quarter == 4:
    print("Диапазон возможных координат: x > 0, y < 0")
if quarter == 2:
    print("Диапазон возможных координат: x < 0, y > 0")
if quarter < 1 or quarter > 4:
    print("Введите корректные координаты точек")