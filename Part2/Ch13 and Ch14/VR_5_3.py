from tkinter import *
import random
import time
import pickle


tk = Tk()
tk.title("гра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
my_image = PhotoImage(file="космос.png", width=500, height=500)
canvas.create_image(0, 0, anchor=NW, image=my_image)
canvas.create_text(15, 5, text="счет:", fill="violet")
canvas.create_text(55, 5, text="рекорд:", fill="violet")
canvas.pack()
tk.update()

sp_x_1_paddle = -4
sp_x_2_paddle = 4


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(-10, -10, 10, 10, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.sp_y_1 = 3
        self.sp_y_2 = -3
        self.sp_x_1 = 3
        self.sp_x_2 = -3
        self.text_x = 0

        self.print_scores()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if self.hit_paddle(pos) == True:
            canvas.delete(self.text)
            canvas.delete(self.text_2)
            self.text_x = self.text_x + 1

            self.print_scores()

            self.sp_y_1 = self.sp_y_1 + 0.02
            self.sp_y_2 = self.sp_y_2 - 0.02
            self.sp_x_1 = self.sp_x_1 + 0.02
            self.sp_x_2 = self.sp_x_2 - 0.02
            tk.update_idletasks()
            tk.update()

            self.y = self.sp_y_2
        if pos[1] <= 0:
            self.y = self.sp_y_1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = self.sp_x_1
        if pos[2] >= self.canvas_width:
            self.x = self.sp_x_2

    def print_scores(self):
        self.text = canvas.create_text(27, 17, text=self.text_x, fill="violet")
        content = open("rk.txt", "r").read()
        if self.text_x > int(content):
            file = open("rk.txt", "w")
            file.write(str(self.text_x))
            file.close()
            content = self.text_x

        self.text_2 = canvas.create_text(67, 17, text=content, fill="violet")


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(-25, 0, 125, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)


    def turn_left(self, evt):
        self.x = sp_x_1_paddle

    def turn_right(self, evt):
        self.x = sp_x_2_paddle

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0

        elif pos[2] >= self.canvas_width:
            self.x = -0


paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

Time = 3
for __for__ in range(0, 3):
    text = canvas.create_text(250, 230, text=Time, font=("Helvetica", 40))
    tk.update()
    time.sleep(1)
    canvas.delete(text)
    Time = Time - 1


while 1:
    if ball.hit_bottom == False:
        ball.draw()
    if ball.hit_bottom == True:
        canvas.create_text(250, 200, text="кінец гри", font=("courier", 26))
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
