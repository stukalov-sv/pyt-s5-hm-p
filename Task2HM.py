# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def type_game_choose() -> int:
    print('New game\n1 - P vs P\n2 - P vs Easy bot\n3 - P vs Mind bot')
    game_type = int(
        input('Enter number of game (1, 2, 3): '))
    return game_type


def players_names(player_number: int) -> str:
    player_name = str(
        input(f'Hello, player. Enter your name, please, or push "Enter" and you will be "Player #{player_number}": '))
    if player_name == '':
        player_name = f'Player #{player_number}'
    return player_name


def first_turn_tossup() -> bool:
    toss = False
    if (random.randint(1, 9) % 2 == 0):
        toss = True
    return toss


def player_turn(player_name: str) -> int:
    turn = int(
        input(f'{player_name}, how many candies to 28 you take? '))
    return turn


def basic_bot_player() -> int:
    bot_turn = random.randint(1, 28)
    return bot_turn


def mind_bot_player(player_turn: int) -> int:
    bot_turn = 29 - player_turn
    return bot_turn


def p_vs_p_game(candies_sum: int) -> bool:
    winner = True

    while candies_sum > 0:
        correct_first = False
        correct_second = False

        first_player = player_turn(first_name)
        if first_player < 29:
            winner = True
            correct_first = True
            print(f'{first_name} take: {first_player}')
            candies_sum -= first_player
            print(f'Candies left: {candies_sum}')
        else:
            print('Incorrect data')

        if (candies_sum > 1 and correct_first):
            while not correct_second:
                second_player = player_turn(second_name)
                if second_player < 29:
                    winner = False
                    correct_second = True
                    print(f'{second_name} take: {second_player}')
                    candies_sum -= second_player
                    print(f'Candies left: {candies_sum}')
                else:
                    print('Incorrect data')
    return winner


def p_vs_basic_bot(candies_sum: int, tossup: bool) -> bool:
    winner = True

    while candies_sum > 0:
        while tossup:
            first_player = player_turn(first_name)
            winner = True
            if first_player < 29:
                tossup = False
                print(f'{first_name} take: {first_player}')
                candies_sum -= first_player
                print(f'Candies left: {candies_sum}')
            else:
                print('Incorrect data')

        if (candies_sum > 1 and not tossup):
            if (candies_sum < 29):
                winner = False
                candies_sum -= candies_sum
            else:
                bot_player = basic_bot_player()
                tossup = True
                print(f'Computer take: {bot_player}')
                candies_sum -= bot_player
                print(f'Candies left: {candies_sum}')
    return winner


def p_vs_mind_bot(candies_sum: int, tossup: bool, first_bot_turn: bool) -> bool:
    winner = True

    while candies_sum > 0:
        while tossup:
            winner = True
            first_player = player_turn(first_name)
            if first_player < 29:
                tossup = False
                print(f'{first_name} take: {first_player}')
                candies_sum -= first_player
                print(f'Candies left: {candies_sum}')
            else:
                print('Incorrect data')

        if (candies_sum > 0 and not tossup):
            if (first_bot_turn):
                bot_player = 20
                tossup = True
                print(f'Computer take: {bot_player}')
                candies_sum -= bot_player
                print(f'Candies left: {candies_sum}')
                first_bot_turn = False
            elif (candies_sum < 29):
                winner = False
                candies_sum -= candies_sum
            else:
                bot_player = mind_bot_player(first_player)
                tossup = True
                print(f'Computer take: {bot_player}')
                candies_sum -= bot_player
                print(f'Candies left: {candies_sum}')
    return winner


# Для проверки выигрышной стратегии игрока №1 можно использовать 107,
# чтобы уменьшить количество итераций игры, при этом игра будет аналогична игре с числом 2021 ->
# первый игрок победит, если возьмет 20 конфет в начале, а потом будет добивать до 29 любую пару
# взяток. И в итоге он в любом случае будет брать последним


game_type = type_game_choose()
candies_sum = 107
tossup = first_turn_tossup()

if (game_type == 1):
    first_name = players_names(1)
    second_name = players_names(2)

    if (tossup):
        print(f'{second_name}, first turn is yours')
        temp_name = first_name
        first_name = second_name
        second_name = temp_name
    else:
        print(f'{first_name}, first turn is yours')

    winner = p_vs_p_game(candies_sum)

    if winner:
        print(f'Game over. {first_name} won. Congratulation!')
    else:
        print(f'Game over. {second_name} won. Congratulation!')
elif (game_type == 2):
    first_name = players_names(1)

    if (tossup):
        print(f'{first_name}, first turn is yours')
    else:
        print('Computer turn first')

    winner = p_vs_basic_bot(candies_sum, tossup)

    if winner:
        print(f'Game over. {first_name} won. Congratulation!')
    else:
        print(f'Game over. Unfortunately, computer won. Please, try again')
elif (game_type == 3):
    first_name = players_names(1)

    if (tossup):
        first_bot_turn = False
        print(f'{first_name}, first turn is yours')
    else:
        first_bot_turn = True
        print('Computer turn first')

    winner = p_vs_mind_bot(candies_sum, tossup, first_bot_turn)

    if winner:
        print(f'Game over. {first_name} won. Congratulation!')
    else:
        print(f'Game over. Unfortunately, computer won. Please, try again')
else:
    print('Incorrect data. Try again')
