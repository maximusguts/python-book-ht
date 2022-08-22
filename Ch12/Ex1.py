import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=900, height=600)
canvas.pack()

text = canvas.create_text(750, 30, text="Трикутників:")

x = 0
while True:
    x = x + 1
    text = canvas.create_text(750, 50, text=x)
    canvas.create_polygon(random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          random.randint(0, 600),
                          fill="green",
                          outline="black")

    tk.update()
    canvas.delete(text)
