from  turtle import *
bgcolor('black')
speed("fast")
clrlist = ['purple','white']
for i in range (100):
  color(clrlist[i%2])
  forward(i*2)
  left(90)
mainloop()