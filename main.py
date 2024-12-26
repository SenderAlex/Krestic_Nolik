import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('350x300')

current_player = 'X'
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


def on_click_mouse(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo('Игра окончена', f'Игрок {current_player} победил!!!')

    current_player = "0" if current_player == "X" else "X"


window.mainloop()