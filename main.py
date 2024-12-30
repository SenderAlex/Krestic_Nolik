import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('550x400')

current_player = "X"
buttons = []

X_player_wins = 0
O_player_wins = 0


def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return buttons[2][0]['text']

    return None


def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                return False
    return True


def on_click_mouse(row, col):
    global current_player, X_player_wins, O_player_wins

    if buttons[row][col]['text'] != "":  # проверка на то, чтобы не перезаписывалась ячейка, т.е.
        # поверх крестика или нолика не записывалось еще что-то
        return
    buttons[row][col]['text'] = current_player

    winner = check_winner()

    if winner:
        if winner == "X":
            X_player_wins += 1
            update_score()
        else:
            O_player_wins += 1
            update_score()
        messagebox.showinfo('Игра окончена', f'Игрок {winner} победил. '
                                             f'Счет в серии {X_player_wins}:{O_player_wins}')
        if X_player_wins == 3 or O_player_wins == 3:
            messagebox.showinfo('Серия завершена!!!', f'Игрок {winner} выиграл серию. '
                                             f'Счет в серии {X_player_wins}:{O_player_wins}')
            clear_score()
        else:
            clear_button()

    elif check_draw():
        messagebox.showinfo('Игра окончена', f'Ничья. Счет прежний {X_player_wins}:{O_player_wins}')
        clear_button()

    current_player = "0" if current_player == "X" else "X"


def reset_game():
    global current_player, X_player_wins, O_player_wins
    X_player_wins = 0
    O_player_wins = 0
    current_player = "X"
    clear_button()


def clear_button():
    for row in buttons:
        for button in row:
            button['text'] = ""

def choosing_x_or_0():
    dialog = tk.Toplevel(window)
    dialog.title('Выберите "крестик" или "нолик"')

    label = tk.Label(dialog, text='Сделайте свой выбор')
    label.pack(pady=5)

    entry = tk.Entry(dialog, width=10)
    entry.pack(pady=5)

    def submit():
        global current_player
        current_player = entry.get()
        if current_player == "X" or current_player == "0":
            messagebox.showinfo('Выбор игрока', f'Вы выбрали {current_player}')
        else:
            messagebox.showinfo('Выбор игрока', f'Ошибка!! Выдолжны выбрать либо "X" либо "0"')
        dialog.destroy()

    button_frame = tk.Frame(dialog)  # чтобы кнопки ok_button и cancel_button были по середине окна
    button_frame.pack(pady=10)

    ok_button = tk.Button(button_frame, text="OK", command=submit)
    ok_button.pack(side=tk.LEFT, padx=4, pady=10)
    cancel_button = tk.Button(button_frame, text="Cancel", command=dialog.destroy)
    cancel_button.pack(side=tk.RIGHT, padx=4, pady=10)


for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 20), bg='lightgray', fg='red', height=2, width=4,
                           command=lambda r=i, c=j: on_click_mouse(r, c))
        button.grid(row=i, column=j, padx=20, pady=20)
        row.append(button)
    buttons.append(row)

reset_button = tk.Button(text="Сброс", height=2, width=8, font=('Arial', 11, 'bold italic'), bg="lightgray",
                         fg="purple", command=clear_button)
reset_button.grid(row=0, column=4, padx=50)

select_button = tk.Button(text="Выбери 'X' или '0' ", height=2, width=15, font=('Arial', 11, 'bold italic'),
                          bg="lightgray", fg="purple", command=choosing_x_or_0)
select_button.grid(row=1, column=4, padx=50)


score = tk.Button(text=f"СЧЕТ\n Крестик Нолик\n{X_player_wins}:{O_player_wins}",
                  height=4, width=15, font=('Arial', 11, 'bold italic'), bg="lightgray", fg="purple")
score.grid(row=2, column=4)


def update_score():
    score.config(text=f'СЧЕТ\n Крестик Нолик\n{X_player_wins}:{O_player_wins}')

def clear_score():
    reset_game()
    score.config(text=f'СЧЕТ\n Крестик Нолик\n{X_player_wins}:{O_player_wins}')


window.mainloop()