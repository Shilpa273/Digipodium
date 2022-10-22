from turtle import *
import colorsys
bgcolor("black")
speed("fastest")
h=0
def draw(angle,n):
    circle(90+n,70)
    lt(angle)
    circle(90+n,60)
pensize(3)
goto(-50,0)
for i in range(300):
    c= colorsys.hsv_to_rgb(h,0.9,0.9)
    h+= 0.005
    pencolor(c)
    draw(90,i)
    draw(120,i)
    draw(180,i)
    draw(90,i)
done()        