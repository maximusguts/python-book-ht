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
        self.bg = PhotoImage(file="GIMP/background/background.png")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor="nw")
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


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def within_x(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.y1 >= co2.y1:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co2.y2 >= co2.y2 and co1.y1 >= co2.y1:
            return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_cals = co1.y2 + y
        if y_cals >= co2.y1 and y_cals <= co2.y1:
            return True
    return False


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.cordinates = None

    def move(self):
        pass

    def coords(self):
        return self.cordinates

class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
        self.coordinates = Coords(x, y, x + width, y + height)


g = Game()
platform1 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform3.png"), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform3.png"), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform3.png"), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform3.png"), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform2.png"), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform2.png"), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform2.png"), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform2.png"), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform1.png"), 170, 250, 33, 10)
platform10 = PlatformSprite(g, PhotoImage(file="GIMP/platform/platform1.png"), 230, 200, 33, 10)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)
g.mainloop()
