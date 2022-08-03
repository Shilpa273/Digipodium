from turtle import *
speed('fastest')
bgcolor('black')
pensize(3)
pencolor('green')

for i in range(8): #outer loop
    pencolor('deeppink')
    fd(150)
    lt(360/8)

    
    for i in range(8): #inner loop
        pencolor('deepskyblue')
        fd(80)
        lt(360/8)
        

mainloop()    