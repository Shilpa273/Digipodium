from turtle import *
speed("fastest")
pensize(1)
bgcolor("black")
hideturtle()
pencolor("red")
colors = ["yellow", "red","yellow","red"]
for i in range(120):
    for c in colors:
        color(c)
        circle(200-i,100)
        lt(90)
        circle(200-i,100)
        rt(60)
        end_fill()
mainloop()       