# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
 
 
# man vs smart bot
import random
from random import randint, choice
 
print(
    '"Игра с конфетами"\n'
    'В игре участвуют два игрока\n'
    'Первый ход определяется жеребьевкой.\n'
    'Игроки ходят, совершая ход друг после друга\n'
    'Правила игры\n'
    'У нас есть некоторое количество конфет\n'
    'За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n'
    'Тот, кому достанется последняя конфета - проиграл\n'
    )
 
messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'Ваш ход']
sweets = 0
max_number_move = 0
player1 = ''
player2 = ''
first = random.randint(0, 1)
def introduce_players():
    global player1
    global player2
    player1 = input('Первый игрок, представьтесь:\n')
    player2 = input('Второй игрок, представьтесь:\n')
    print(f'Очень приятно!\n'
          f'Битва между {player1} и {player2} началась!')
    return [player1, player2]
 
def introduce_players_Bot():
    global player1
    global player2
    player1 = input('Первый игрок, представьтесь:\n')
    player2 = 'BOT'
    print(f'Очень приятно!\nCегодня Вы играете с {player2}!')
    return [player1, player2]
 
def introduce_players_smartBot():
    global player1
    global player2
    player1 = input('Первый игрок, представьтесь:\n')
    player2 = 'SmartBOT'
    print(f'Очень приятно!\nCегодня Вы играете со {player2}!')
    return [player1, player2]
 
def sweets_game(players):
    global sweets
    global max_number_move
    global player1
    global player2
    sweets = int(input('Введите cколько всего у нас конфет:\n'))
    max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
    first = int(random.randint(0, 1))
    if first == 1:
        print(f'\nПервый ход определён жеребьёвкой, начинает {player1}!')
    else:
        print(f'\nПервый ход определён жеребьёвкой, начинает {player2}!')
 
    players[0] = players[first-1]
    return [sweets, max_number_move, int(first)]
 
#max_move = max_number_move
 
###friends_vs_friends
def game_friends_vs_friends(sweets, players, messages):
    global first
    count = 0
    while sweets[0] > 0:
        move = int(input(f'{players[first%2]}, {random.choice(messages)}:'))
        if move > sweets[0] or move > max_number_move:
            print(f'Можно взять не более {max_number_move} конфет, у нас всего {sweets[0]} конфет')
            chance = 2
            while chance > 0:
                if sweets[0] >= move <= max_number_move:
                    break
                print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                move = int(input())
                chance -= 1
            else:
                return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        first += 1
        count += 1
    return players[first % 2]
###friends_vs_friends
 
### Bot
def game_player_vs_bot(sweets, players, messages):
    global max_number_move
    count = sweets[2]
 
    while sweets[0] > 0:
        if not count % 2:
            move = random.randint(1, sweets[1])
            print(f'BOT: Я забираю {move} шт.')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]
### Bot
 
### SmartBot
def game_player_vs_smart_bot(sweets, players, messages):
    global max_number_move
    count = sweets[2]
 
    while sweets[0] > 0:
        if sweets[0] == max_number_move:
            move = sweets[0] -1
            print(f'SmartBOT: Я забираю {move} шт.')
        elif (sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] - 1
            print(f'SmartBOT: Я забираю {move} шт.')
 
        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'SmartBOT: Я забираю {move} шт.')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]
### SmartBot
 
mode_game = input('Выберите режим игры:\n'
                  '1 - игра с другом\n'
                  '2 - игра против бота\n'
                  '3 - игра с "умным" ботом\n')
 
if not mode_game.isdigit():
    print("Неверный ввод, введите число от 1 до 3 ")
elif mode_game == '1':
    print('Вы выбрали игру с другом')
    players = introduce_players()
    sweets = sweets_game(players)
    winer = game_friends_vs_friends(sweets, players, messages)
    if not winer:
        print('Доигрались! У нас нет победителя.')
    else:
        print(
            f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
elif mode_game == '2':
    print('Вы выбрали игру с ботом ')
    players = introduce_players_Bot()
    sweets = sweets_game(players)
    winer = game_player_vs_bot(sweets, players, messages)
    if not winer:
        print('Доигрались! У нас нет победителя.')
    else:
        print(
            f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
elif mode_game == '3':
    print('Вы выбрали игру с ботом ')
    players = introduce_players_smartBot()
    sweets = sweets_game(players)
    winer = game_player_vs_smart_bot(sweets, players, messages)
    if not winer:
        print('Доигрались! У нас нет победителя.')
    else:
        print(
            f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')