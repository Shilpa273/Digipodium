from turtle import *
speed("fastest")
bgcolor("black")
clrlist = ['red','yellow','lime']

for i in range(400):
    color(clrlist[i%3])
    lt(i*2)
    circle(120)
    
    
mainloop()    