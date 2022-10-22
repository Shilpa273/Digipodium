from turtle import *
import colorsys
bgcolor("black")
speed("fastest")
h=0
def ninja(angle,n):
    circle(20+n,90)
    left(angle) 
    circle(i+n,60)
    circle(i,90)
goto(0,0)
for i in range(300):
    c= colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    ninja(90,i)
    ninja(-90,i)
    h+=0.005
done()        