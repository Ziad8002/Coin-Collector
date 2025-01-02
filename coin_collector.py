import pgzrun
import pgzero
from pgzero.builtins import Actor
import random
screen:pgzero.screen.Screen
WIDTH=700
HEIGHT=700
TITLE="Collect the coins"
fox=Actor("fox.png")
coin=Actor("coin.png")
power_up=Actor("power_up.png")
power_up.pos=100,100
fox.pos=WIDTH/2,HEIGHT/2
coin.pos=WIDTH/2+100,HEIGHT/2+100
score=0
time=30
high_score=0
gameOver=False
speed=4
def update_time():
    global time,gameOver
    if time<=0:
        gameOver=True
    else:
        time -= 1
clock.schedule_interval(update_time, 1)
def speed_reset():
    global speed
    speed=4
def draw():
    global gameOver,score,high_score
    if not gameOver:
        screen.clear()
        screen.blit("background.png",(0,0))
        screen.draw.text("Collect the Coins!!",(WIDTH/2-100,10))
        screen.draw.text(f'Score : {score}',(600,10))
        screen.draw.text(f'Time : {time}',(10,10))
        fox.draw()
        coin.draw()
    else:
        screen.fill("maroon")
        screen.draw.text("GAME OVER",(25,HEIGHT/2-200),fontsize=150)
        screen.draw.text(f"Score: {score}",(270,250),fontsize=40)
        screen.draw.text(f"High Score: {high_score}",(270,280),fontsize=40)
        screen.draw.text("Retry???",(270,310),fontsize=40)
        screen.draw.text("Quit?",(270,340),fontsize=40)

def update():
    global score,time,gameOver,high_score,speed
    if keyboard.Right:
        if fox.x<WIDTH:
            fox.x+=speed
        else:
            fox.x=0
    if keyboard.LEFT:
        if fox.x>0:
            fox.x-=speed
        else:
            fox.x=WIDTH
    if keyboard.UP:
        if fox.y>0:
            fox.y-=speed
        else:
            fox.y=HEIGHT
    if keyboard.DOWN:
        if fox.y<HEIGHT:
            fox.y+=speed
        else:
            fox.y=0
    if fox.colliderect(coin):
        coin.x =random.randint(0,WIDTH)
        coin.y =random.randint(0,HEIGHT)
        score+=1
        time+=1
        speed=8
        clock.schedule(speed_reset,3)
    # if score%2==0:
    #     power_up.draw()
    #     if fox.colliderect(power_up):
    #         power_up.x =random.randint(0,WIDTH)
    #         power_up.y =random.randint(0,HEIGHT)
    #         score+=5
    #         time+=5
    #         speed=8
    #         clock.schedule(speed_reset,3)
    if keyboard.R:
        gameOver=False
        time=10
        score=0
    if score>high_score:
        high_score=score
    if keyboard.Q:
        quit()
    power_up.draw()
pgzrun.go()
