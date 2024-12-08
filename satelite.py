import pgzrun,random
from time import time

WIDTH = 800
HEIGHT = 800

satelites = []
lines = []

nextSatelite = 0
noOfSatelites = random.randint(5,8)

startTime = 0
totalTime = 0
endTime = 0

def createSatelite():
    global startTime
    
    for i in range(noOfSatelites):
        satelite = Actor("satelite")
        satelite.pos = random.randint(50, WIDTH-50),random.randint(50, HEIGHT-50)
        satelites.append(satelite)
        
    startTime = time()       

def draw():
    global totalTime
    n = 1
    
    screen.blit("space", (0,0))
    
    for i in satelites:
        screen.draw.text(str(n), (i.pos[0], i.pos[1]+20))
        i.draw()
        n += 1
        
    for i in lines:
        screen.draw.line(i[0], i[1], (255, 255, 255))
        
    if nextSatelite < noOfSatelites:
        totalTime = time()-startTime
        screen.draw.text(str(round(totalTime, 1)), (20, 20), fontsize = 30)
    else:
        screen.draw.text(str(round(totalTime, 1)), (20, 20), fontsize = 30)                           
    
    print(lines)
def update():
    pass

def on_mouse_down(pos):
    global nextSatelite, lines
    
    if nextSatelite < noOfSatelites:
        if satelites[nextSatelite].collidepoint(pos):
            if nextSatelite:
                lines.append((satelites[nextSatelite-1].pos, satelites[nextSatelite].pos))
                print(lines)
                # make sure we will increase the next satelite else it wont find first one at all 
            nextSatelite+=1
            else:
                nextSatelite = 0
                lines = []

createSatelite()
pgzrun.go()                       
