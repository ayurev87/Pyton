#  Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

numb_list_1 = ['1', '3', '5', '1']  # создаём 1-й список строк и записываем его в файл 1
data1 = open('file_33_1.txt', 'w')
data1.writelines(numb_list_1)
data1.close()


numb_list_2 = ['2', '6', '4', '3']  # создаём 2-й список строк и записываем его в файл 2
data2 = open('file_33_2.txt', 'w')
data2.writelines(numb_list_2)
data2.close()


data3 = open('file_33_1.txt', 'r')   # распаковываем список 1, переводим его в int и создаём новый список
s = data3.readline()
n = int(s)
result1 = []
while n > 0:
    result1.append(n % 10)
    n //= 10

result1.reverse()
print(f'Распакованный список из "файла 1" : {result1}')
print()
data3.close()


data4 = open('file_33_2.txt', 'r')  # распаковываем список 2, переводим его в int и создаём новый список
s1 = data4.readline()
n1 = int(s1)
result2 = []
while n1 > 0:
    result2.append(n1 % 10)
    n1 //= 10

result2.reverse()
print(f'Распакованный список из "файла 2" : {result2}')
print()
data4.close()

sum_arr = []                # складываем элементы списка 1 и списка 2 между собой, и выводим в новый список
for i in range(len(result1)):
    sum_arr.append(result1[i] + result2[i])
print(f'Суммируем элементы списка из "файла 1" и "файла 2": {sum_arr}')
print()


str_out = []                # переводим список int в  список str           
for element in sum_arr:
    str_out.append(str(element))


print(f'Конвертируем список сумм элементов в строку: {str_out}')
print()


data5 = open('file_33_3.txt', 'w')    # Записываем полученный результат в файл 3
data5.writelines(str_out)
data5.close()