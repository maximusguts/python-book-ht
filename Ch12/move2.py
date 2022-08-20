from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill="red")
canvas.itemconfig(my_triangle, fill="blue")
canvas.itemconfig(my_triangle, outline="red")

mainloop()
