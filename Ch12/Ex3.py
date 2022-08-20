import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
my_image = PhotoImage(file="школа кв.png", width=600, height=600)
canvas.create_image(0, 0, anchor=NW, image=my_image)

while True:
    for x in range(0, 300):
        canvas.move(1, 0, 1)
        time.sleep(0.01)
        tk.update()
    for x in range(0, 300):
        canvas.move(1, 0, -1)
        time.sleep(0.01)
        tk.update()
