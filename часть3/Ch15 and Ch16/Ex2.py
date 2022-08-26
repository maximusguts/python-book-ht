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
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5, 2):
            for y in range(0, 5, 2):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor="nw")
        for x in range(1, 5, 2):
            for y in range(1, 5, 2):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor="nw")
        self.canvas.create_image(100, 0, image=self.bg2, anchor="nw")
        self.canvas.create_image(300, 0, image=self.bg2, anchor="nw")
        self.canvas.create_image(0, 100, image=self.bg2, anchor="nw")
        self.canvas.create_image(200, 100, image=self.bg2, anchor="nw")
        self.canvas.create_image(400, 100, image=self.bg2, anchor="nw")
        self.canvas.create_image(100, 200, image=self.bg2, anchor="nw")
        self.canvas.create_image(300, 200, image=self.bg2, anchor="nw")
        self.canvas.create_image(0, 300, image=self.bg2, anchor="nw")
        self.canvas.create_image(200, 300, image=self.bg2, anchor="nw")
        self.canvas.create_image(400, 300, image=self.bg2, anchor="nw")
        self.canvas.create_image(100, 400, image=self.bg2, anchor="nw")
        self.canvas.create_image(300, 400, image=self.bg2, anchor="nw")

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
