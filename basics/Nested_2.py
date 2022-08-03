from turtle import *
speed('fastest')

pensize(5)
bgcolor('black')
for i in range(4):
    pencolor('maroon')
    fd(200)
    lt(360/4)
    for i in range(10):
        pencolor('lime')
        circle(i*15)
        
mainloop()   