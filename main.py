import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('800x600')

current_player = "X"
buttons = []


def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return True

    return False


def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                return False

    # проверка по горизонтали
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return False

    # проверка по вертикали
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] != "":
            return False

    # проверка по диагоналям
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return False

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return False

    return True


def on_click_mouse(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo('Игра окончена', f'Игрок {current_player} победил!!!')
    if check_draw():
        messagebox.showinfo('Игра окончена', f'Ничья!!!')

    current_player = "0" if current_player == "X" else "X"

def clear_button():
    global current_player
    current_player = "X"

    for row in buttons:
        for button in row:
            button['text'] = ""

def choosing_x_or_0():
    dialog = tk.Toplevel(window)
    dialog.title('Выберите "крестик" или "нолик"')

    label = tk.Label(dialog, text='Сделайте свой выбор')
    label.pack(pady=5)

    entry = tk.Entry(dialog, width=30)
    entry.pack(pady=5)

    def submit():
        global current_player
        current_player = entry.get()
        if current_player == "X" or current_player == "0":
            messagebox.showinfo('Выбор игрока', f'Вы выбрали {current_player}')
        else:
            messagebox.showinfo('Выбор игрока', f'Ошибка!! Выдолжны выбрать либо "X" либо "0"')
        dialog.destroy()

    ok_button = tk.Button(dialog, text="OK", command=submit)
    ok_button.pack(side=tk.LEFT, padx=10, pady=10)
    cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
    cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)


for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 20), height=2, width=4,
                           command=lambda r=i, c=j: on_click_mouse(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

reset_button = tk.Button(text="Сброс", height=2, width=8, font=('Arial', 9, 'bold'), command=clear_button)
reset_button.grid(row=4, column=0)

select_button = tk.Button(text="Выбери 'X' или '0' ", height=2, width=8, font=('Arial', 9, 'bold'),
                          command=choosing_x_or_0)
select_button.grid(row=4, column=1)



window.mainloop()

