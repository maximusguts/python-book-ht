from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("містер Руки-палички біжить до виходу")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file="GIMP/тло/тло.png")
        self.bg2 = PhotoImage(file="GIMP/тло/тло для зявданя.png")
        self.bg3 = PhotoImage(file="завд.png")
        w = self.bg.width()
        h = self.bg.height()
        images = {
            1: self.bg,
            2: self.bg2,
            3: self.bg3
        }
        number = 1
        for x in range(0, 5):
            for y in range(0, 5):
                number += 1
                if number > 3:
                    number = 1
                self.canvas.create_image(x * w, y * h, image=images[number], anchor="nw")



        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


g = Game()
g.mainloop()
