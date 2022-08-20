from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_text(150, 100, text="жив собі хлопець в молдові,")
canvas.create_text(130, 120, text="катався кругом на корові,", fill="red")
canvas.create_text(150, 150, text="так-от, каже, біда,", font=("Times", 15))
canvas.create_text(200, 200, text="і зовсім вона не одна:", font=("Helvetica", 20))
canvas.create_text(220, 250, text="тата возять", font=("courier", 22))
canvas.create_text(220, 300, text="дві курки здорові!", font=("courier", 26))

mainloop()
