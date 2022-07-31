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
            turns_list_first.append(btn.winfo_x() + btn.winfo_y())
            button_config(btn, 'x')
            turn_count = False

        elif (not turn_count):
            turns_list_second.append(btn.winfo_x() + btn.winfo_y())
            button_config(btn, 'o')
            turn_count = True

    else:
        button_config(btn, ' ')

    if (winner_check(btn.winfo_reqwidth(), btn.winfo_reqheight(), turns_list_first)):
        print(f'Game over. {first_name} won. Congratulation!')
        end_game = True
    elif (winner_check(btn.winfo_reqwidth(), btn.winfo_reqheight(), turns_list_second)):
        print(f'Game over. {second_name} won. Congratulation!')
        end_game = True


def element_check(number: int, checked_list: list) -> bool:
    check = False

    if (any(element == number for element in checked_list)):
        check = True

    return check


def task_check(f_number: int, s_number: int, t_number: int, checked_list: list) -> bool:
    check = False

    if (element_check(f_number, checked_list) and
        element_check(s_number, checked_list) and
        element_check(t_number, checked_list)):
        check = True

    return check


def winner_check(width: int, height: int, turns_list: list) -> bool:
    winner = False

    if (task_check(0, width, width * 2, turns_list) or
        task_check(height, height + width, height + width * 2, turns_list) or
        task_check(height * 2, height * 2 + width, height * 2 + width * 2, turns_list) or
        task_check(0, height, height * 2, turns_list) or
        task_check(width, width + height, width + height * 2, turns_list) or
        task_check(width * 2, width * 2 + height, width * 2 + height * 2, turns_list) or
        task_check(0, width + height, width * 2 + height * 2, turns_list) or
        task_check(height * 2, width + height, width * 2, turns_list)):
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
        btn.grid(column=y, row=x)

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
