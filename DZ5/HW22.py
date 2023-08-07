# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

import random


current_player = random.randint(1, 2)
kan = 2021
print(f'На столе {kan} конфет')


def getPlayerInput(is_bot,kan):
    if is_bot:
        answer = random.randint(1,29)
    else:
        answer = input('Введите количество конфет: ')
    return answer


while kan > 0:
    print(f'Сейчас ходит игрок {current_player}')
    n = int(getPlayerInput(current_player==2,kan))
    n = min(n, 28)
    kan = kan - n
    print(f'Теперь {kan} конфет')  
    if kan <= 0:
        print(f'Игрок {current_player} выиграл !') 
        break 
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1