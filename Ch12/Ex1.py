import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
while True:
    canvas.create_polygon(random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          fill="green",
                          outline="black")
    tk.update()
