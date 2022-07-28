# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Тот, кто берет последнюю конфету - проиграл.
# игра с другом


import random

print(
    '"Игра с конфетами"\n В игре участвуют два игрока\n Первый ход определяется жеребьевкой. \n'
     'Игроки ходят, совершая ход друг после друга \n'
     'Правила игры\n'
     'У нас есть некоторое количество конфет\n'
     'За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n'
     'Тот, кому достанется последняя конфета - проиграл\n'
    ) 

messages = ['Ваш ход брать конфеты', 'Возьмите конфеты', 
            'сколько конфет берем?', 'берите еще', 'Ваш ход']

def game_friends_vs_friends(total_sweets, max_number_move, players, messages):
    count = 0
    if total_sweets%10 == 1 and 9 > total_sweets > 10: letter = 'а'
    elif 1 < total_sweets%10 < 5 and 9 > total_sweets > 10: letter = 'ы'
    else: letter = ''
    while total_sweets > 0:
        print(f' {players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > total_sweets or move > max_number_move:
            print(f'Можно взять не более {max_number_move} конфет{letter}, у нас всего {total_sweets} конфет{letter}')
            chance = 2
            while chance > 0:
                if total_sweets >= move <= max_number_move:
                    break
                print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                move = int(input())
                chance -=1
            else: 
                return print(f'Попыток не осталось. Game over!')
        total_sweets = total_sweets - move
        if total_sweets > 0: print(f'Осталось {total_sweets} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

player1 = input('Первый игрок, как к Вам можно обращаться?\n')
player2 = input('Второй игрок, Ваше имя?\n')
players = [player1, player2]

total_sweets = int(input('Введите cколько всего у нас конфет:\n '))
max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n '))

winer = game_friends_vs_friends(total_sweets, max_number_move, players, messages)
if not winer:
    print('Победителя нет.')
else: print(f'Поздравляю! Победил {winer}!')