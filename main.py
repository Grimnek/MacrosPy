from tkinter import Tk, StringVar, Label, Button, Menu, Entry, messagebox
import pyautogui as pag
import keyboard
from time import sleep

width = 400
height = 400

root = Tk()
root.title("MacrosPy")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)


def afk():
    stop_key = message.get()
    try:
        while True:
            pag.keyDown('w')
            sleep(0.5)
            pag.keyUp('w')
            pag.keyDown('d')
            sleep(0.5)
            pag.keyUp('d')
            pag.keyDown('s')
            sleep(0.5)
            pag.keyUp('s')
            pag.keyDown('a')
            sleep(0.5)
            pag.keyUp('a')

            if keyboard.is_pressed(stop_key):
                break
    except ValueError:
        messagebox.showerror("Помилка", "Заповніть поля")


def autoclick():
    stop_key = message.get()
    key = message_1.get()
    try:
        left = ('Left', 'left', 'лкм', 'ЛКМ')
        right = ('ПКМ', 'пкм', 'right', 'Right')
        middle = ('СКМ', 'скм', 'middle', 'Middle')

        while True:
            if key in left:
                pag.click(button='left')
            if key in right:
                pag.click(button='right')
            if key in middle:
                pag.click(button='middle')
            else:
                pass

            if keyboard.is_pressed(stop_key):
                break
    except ValueError:
        messagebox.showerror("Помилка", "Заповніть поля")


def autopush():
    stop_key = message.get()
    key = message_1.get()
    try:
        while True:
            pag.keyDown(key)
            pag.keyUp(key)

            if keyboard.is_pressed(stop_key):
                break
    except ValueError:
        messagebox.showerror("Помилка", "Заповніть поля")


def help():
    messagebox.askquestion("Допомога",
                           "1 поле потрібно для кнопки, яка зупинить процес.\n 2 поле потрібно для дії, яка буде виробляти бот, як наприклад:\n \n Буква для автопуша (мається на увазі постійне натискання на клавішу клавіатури) \n \n Left, left, лкм, ЛКМ - Ліва кнопка миші для автоклікера \n ПКМ, пкм, Right, right - Права кнопка миші для автоклікера \n СКМ, скм, middle, Middle - Середня кнопка миші для автоклікера \n \nP.S. AFK функція іноді закривається некоректно. У разі зависання програми - ALT + F4.")


message = StringVar()
message_1 = StringVar()

message_label = Label(text="Впишіть букву для зупинки процесу")
message_label.place(relx=.2, rely=.0)

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="center", width="40", height="25")

message_label1 = Label(text="Впишіть букву або слово для дії")
message_label1.place(relx=.2, rely=.2)

message_entry_1 = Entry(textvariable=message_1)
message_entry_1.place(relx=.5, rely=.3, anchor="center", width="40", height="25")

message_button = Button(text="AFK", padx="20", pady="15", background="#555", foreground="#fff", command=afk)
message_button.place(relx=.5, rely=.5, anchor="center")

message_button_1 = Button(text="Автоклікер", padx="20", pady="15", background="#555", foreground="#fff",
                          command=autoclick)
message_button_1.place(relx=.5, rely=.7, anchor="center")

message_button_1 = Button(text="Автопуш", padx="20", pady="15", background="#555", foreground="#fff", command=autopush)
message_button_1.place(relx=.5, rely=.9, anchor="center")

main_menu = Menu()
main_menu.add_cascade(label="Допомога", command=help)
root.config(menu=main_menu)

root.mainloop()
