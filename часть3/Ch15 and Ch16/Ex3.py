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
        For = 1
        for x in range(0, 5):
            for y in range(0, 5):
                if For == 4:
                    For = 1
                if For == 3:
                    self.canvas.create_image(x * w, y * h, image=self.bg3, anchor="nw")
                    For = 4
                if For == 2:
                    self.canvas.create_image(x * w, y * h, image=self.bg2, anchor="nw")
                    For = 3
                if For == 1:
                    self.canvas.create_image(x * w, y * h, image=self.bg, anchor="nw")
                    For = 2

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
