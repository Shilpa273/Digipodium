import pgzrun

HEIGHT = 500
WIDTH = 600

p = Actor('ironman',(100,100))
speed = 3
def draw():
    screen.clear()
    p.draw()

def update():
   if keyboard.DOWN:
    p.y += speed
   if keyboard.UP: 
    p.y += -speed  


pgzrun.go()    