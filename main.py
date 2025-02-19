from tkinter import Tk, StringVar, Label, Button, Menu, Entry, messagebox
import threading
import pyautogui as pag
import keyboard
import time
from pynput import keyboard

width = 350
height = 400

root = Tk()
root.title("MacrosPy")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)

stop_afk = threading.Event()  # Флаг для остановки


def afk():
	stop_afk.clear()  # Сбрасываем флаг перед запуском
	stop_key = message.get()  # Получаем клавишу остановки

	def on_press(key):
		"""Обработчик нажатия клавиши"""
		try:
			if key.char == stop_key:  # Если нажата стоп-клавиша
				stop_afk.set()  # Останавливаем AFK-цикл
				return False  # Завершаем слушатель сразу же
		except AttributeError:
			pass  # Игнорируем спецклавиши

	def smart_sleep(duration, step=1):
		elapsed = 0
		while elapsed < duration:
			if stop_afk.is_set():  # Проверяем флаг остановки во время задержки
				return
			time.sleep(step)
			elapsed += step

	def afk_loop():
		listener = keyboard.Listener(on_press=on_press)
		listener.start()

		while not stop_afk.is_set():
			pag.keyDown('w')
			smart_sleep(2)
			pag.keyUp('w')

			pag.keyDown('d')
			smart_sleep(2)
			pag.keyUp('d')

			pag.keyDown('s')
			smart_sleep(2)
			pag.keyUp('s')

			pag.keyDown('a')
			smart_sleep(2)
			pag.keyUp('a')

		listener.stop()  # Останавливаем слушатель при выходе из цикла

	thread = threading.Thread(target=afk_loop, daemon=True)
	thread.start()


def autoclick():
	stop_afk.clear()
	stop_key = message.get()
	key = message_1.get()

	left = ('Left', 'left')
	right = ('Right', 'right')
	middle = ('Middle', 'middle')

	def on_press(key_press):
		try:
			if key_press.char == stop_key:
				stop_afk.set()
				return False
		except AttributeError:
			pass

	def smart_sleep(duration, step=1):
		elapsed = 0
		while elapsed < duration:
			if stop_afk.is_set():
				return
			time.sleep(step)
			elapsed += step

	def click_loop():
		listener = keyboard.Listener(on_press=on_press)
		listener.start()

		while not stop_afk.is_set():
			if key in left:
				pag.click(button='left')
			elif key in right:
				pag.click(button='right')
			elif key in middle:
				pag.click(button='middle')
			smart_sleep(1)
		listener.stop()

	thread = threading.Thread(target=click_loop, daemon=True)
	thread.start()


def autopush():
	stop_afk.clear()
	stop_key = message.get()
	key = message_1.get()

	def on_press(key_press):
		try:
			if key_press.char == stop_key:
				stop_afk.set()
				return False
		except AttributeError:
			pass

	def smart_sleep(duration, step=0.1):
		elapsed = 0
		while elapsed < duration:
			if stop_afk.is_set():
				return
			time.sleep(step)
			elapsed += step

	def push_loop():
		listener = keyboard.Listener(on_press=on_press)
		listener.start()

		while not stop_afk.is_set():
			pag.keyDown(key)
			smart_sleep(1)
			pag.keyUp(key)
			smart_sleep(0.5)

		listener.stop()

	thread = threading.Thread(target=push_loop, daemon=True)
	thread.start()


def stop_afk_function():
	stop_afk.set()


def help():
	messagebox.showinfo("Help",
	                    "1st field is required for the key that will stop the process."
	                    "\n 2nd field is required for the action that the bot will perform, for example:"
	                    "\n \n A letter for autopush (this means continuous key pressing on the keyboard)."
	                    "\n \n Left, left – Left mouse button for the autoclicker."
	                    "\n Right, right – Right mouse button for the autoclicker."
	                    "\n Middle, middle – Middle mouse button for the autoclicker.")


message = StringVar()
message_1 = StringVar()

message_label = Label(text="Enter a letter to stop the process")
message_label.place(relx=.2, rely=.0)

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="center", width="40", height="25")

message_label1 = Label(text="Enter a letter or word for the action")
message_label1.place(relx=.2, rely=.2)

message_entry_1 = Entry(textvariable=message_1)
message_entry_1.place(relx=.5, rely=.3, anchor="center", width="40", height="25")

message_button = Button(text="AFK", padx="20", pady="15", background="#555", foreground="#fff", command=afk)
message_button.place(relx=.5, rely=.5, anchor="center")

message_button_1 = Button(text="Autoclicker", padx="20", pady="15", background="#555", foreground="#fff",
                          command=autoclick)
message_button_1.place(relx=.5, rely=.7, anchor="center")

message_button_1 = Button(text="Autopush", padx="20", pady="15", background="#555", foreground="#fff", command=autopush)
message_button_1.place(relx=.5, rely=.9, anchor="center")

main_menu = Menu()
main_menu.add_cascade(label="Help", command=help)
root.config(menu=main_menu)

root.mainloop()
