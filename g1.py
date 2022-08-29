import pgzrun

HEIGHT = 400
WIDTH = 600
p = Actor('ironman', pos = (100,100))

def draw():
    screen.clear()
    screen.draw.text("welcome to pgzero", (10,10), color= 'red', fontsize= 50)
    screen.draw.text("created by Shilpa", (10,360), color = 'white')

    p.draw()

#outide function
pgzrun.go()