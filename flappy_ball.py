import pgzrun
import random

WIDTH=500
HEIGHT=600

GRAVITY=1500

class Ball():
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius=radius
        self.vy = 0
        self.vx = 150
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        self.clr = (R,G,B)

    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.clr)

ball1 = Ball(150,200,40)
ball2 = Ball(250,300,80)

def on_key_down(key):
    if key==keys.SPACE:
        ball1.vy = -500

def update(dt):
    uy=ball1.vy
    ball1.vy+=GRAVITY*dt
    ball1.y+=(uy+ball1.vy)*0.5*dt

     # detect and handle bounce
    if ball1.y > HEIGHT - ball1.radius:  # we've bounced!
        ball1.y = HEIGHT - ball1.radius  # fix the position
        ball1.vy = -ball1.vy * 0.9  # inelastic collision
    # X component doesn't have acceleration
   # ball1.x += ball1.vx * dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = -ball1.vx
    
    uy=ball2.vy
    ball2.vy+=GRAVITY*dt
    ball2.y+=(uy+ball1.vy)*0.5*dt

    if ball2.y > HEIGHT - ball2.radius:  # we've bounced!
      ball2.y = HEIGHT - ball2.radius  # fix the position
      ball2.vy = -ball2.vy * 0.9  # inelastic collision
    # X component doesn't have acceleration
   # ball2.x += ball2.vx * dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
      ball2.vx = -ball2.vx

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()

pgzrun.go()