from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=310)
canvas.pack()
my_image = PhotoImage(file="school.png", width=600, height=600)
canvas.create_image(0, 0, anchor=NW, image=my_image)

mainloop()
