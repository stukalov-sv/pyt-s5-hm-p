from tkinter import *
import random


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


def button_click(btn):
    global turns_list_first, turns_list_second, turn_count, end_game

    if not end_game:
        if (turn_count):
            turns_list_first.append(btn.winfo_rootx() + btn.winfo_rooty())
            button_config(btn, 'x')
            turn_count = False
        elif (not turn_count):
            turns_list_second.append(btn.winfo_rootx() + btn.winfo_rooty())
            button_config(btn, 'o')
            turn_count = True
    else:
        button_config(btn, ' ')

    if (winner_check(turns_list_first)):
        print(f'Game over. {first_name} won. Congratulation!')
        end_game = True
    elif (winner_check(turns_list_second)):
        print(f'Game over. {second_name} won. Congratulation!')
        end_game = True

def element_check(number: int, checked_list: list) -> bool:
    check = False

    if (any(element == number for element in checked_list)):
        check = True

    return check


def winner_check(turns_list: list) -> bool:
    winner = False

    if ((element_check(133, turns_list) and element_check(191, turns_list) and element_check(249, turns_list)) or
        (element_check(200, turns_list) and element_check(258, turns_list) and element_check(316, turns_list)) or
        (element_check(267, turns_list) and element_check(325, turns_list) and element_check(383, turns_list)) or
        (element_check(133, turns_list) and element_check(200, turns_list) and element_check(267, turns_list)) or
        (element_check(191, turns_list) and element_check(258, turns_list) and element_check(325, turns_list)) or
        (element_check(249, turns_list) and element_check(316, turns_list) and element_check(383, turns_list)) or
        (element_check(133, turns_list) and element_check(258, turns_list) and element_check(383, turns_list)) or
        (element_check(267, turns_list) and element_check(258, turns_list) and element_check(249, turns_list))):
        winner = True

    return winner


def button_config(btn, sign: str):
    btn.config(state='disabled',
               font=("Lucida Console", 40, "bold"),
               text=f'{sign}')


window = Tk()
window.title('Tic-tac-toe')
window.resizable(width=False, height=False)
frame = Frame(window)
frame.pack()


turn_count = True
end_game = False
turns_list_first = []
turns_list_second = []

for x in range(3):
    for y in range(3):
        btn = Button(frame)
        btn.config(font=("Lucida Console", 40, "bold"),
                   text=' ',
                   command=lambda button=btn: button_click(button))
        btn.grid(column=y, row=x, sticky='nsew')

tossup = first_turn_tossup()

first_name = players_names(1)
second_name = players_names(2)

if (tossup):
    print(f'{second_name}, first turn is yours')
    temp_name = first_name
    first_name = second_name
    second_name = temp_name
else:
    print(f'{first_name}, first turn is yours')

window.mainloop()
