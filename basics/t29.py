from turtle import *
speed("fastest")
bgcolor("black")
colors = ["lime","yellow"]
for i in range(100):
    for c in colors:
        color(c)
        fd(90)
        lt(90)
        circle(200-i,90)
        circle(200-i,100)

        
end_fill()
mainloop()        