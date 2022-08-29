from turtle import *
import colorsys

speed('fastest')
bgcolor("black")
h = 0.1
for i in range (200):
    c = colorsys.hsv_to_rgb(h,1,1,)
    color(c)
    h+=0.005
    begin_fill()
    circle(200 - i,100)
    lt(100)
    circle(200 - i,100)
    rt(100)
    end_fill() 

mainloop()    

 