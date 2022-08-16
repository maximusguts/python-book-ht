import turtle
t = turtle.Pen()
t.begin_fill()
for x in range(0, 8):
    t.color("yellow")
    t.fd(50)
    t.rt(45)
t.end_fill()
for x in range(0, 8):
    t.color("black")
    t.fd(50)
    t.rt(45)