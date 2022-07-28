# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# man vs smart bot

from random import randint, choice

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

def introduce_players():
    player1 = input('Первый игрок, как к Вам можно обращаться?\n')
    player2 = 'SmartBOT'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]

def rules_game(players):
    total_sweets = int(input('Введите cколько всего у нас конфет:\n '))
    max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total_sweets, max_number_move, int(first)]



def game_player_vs_smart_bot(rules, players, messages):
    count = rules[2]
    print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                chance = 2
                while chance > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


players = introduce_players()
rules = rules_game(players)

winer = game_player_vs_smart_bot(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')