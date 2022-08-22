from turtle import *
speed ('fastest')
c = ['green','yellow']
bgcolor('black')

for i in range(500):
    color(c[i%2])
    forward(i*2/2)
    left(360/2 + 1.5)
   

mainloop()    

