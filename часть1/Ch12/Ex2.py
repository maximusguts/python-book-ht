import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.move(1, 150, 150)
while True:
    canvas.move(1, 10, 0)
    time.sleep(0.05)
    tk.update()
    canvas.move(1, 0, 10)
    time.sleep(0.05)
    tk.update()
    canvas.move(1, -10, 0)
    time.sleep(0.05)
    tk.update()
    canvas.move(1, 0, -10)
    time.sleep(0.05)
    tk.update()

