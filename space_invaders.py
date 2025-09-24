import pygame
from pygame.locals import *
import os
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

BORDER=pygame.Rect(WIDTH/2,0,10,HEIGHT)
FPS=60
vel=5
BULLET_VEL=7
spaceship_width,spaceship_height=55,40
YELLOW_SPACESHIP_IMG=pygame.image.load("images/yellow_spaceship.png")
RED_SPACESHIP_IMG=pygame.image.load("images/red_spaceship.png")

SPACE=pygame.transform.scale(pygame.image.load("images/bg2.png"),(WIDTH,HEIGHT))
red_health=10
yellow_health=10

BULLET_HIT=pygame.mixer.Sound("Grenade_sound1.mp3")
BULLET_FIRE=pygame.mixer.Sound("grenade_sound2.mp3")
FONT=pygame.font.SysFont("TimesNewRoman",50)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,image,angle,x,y):
        super().__init__()
        self.image=pygame.transform.rotate(pygame.transform.scale(image,(spaceship_width,spaceship_height)),angle)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

#v=velocity
    def move_horizontal(self,v,player):
        self.rect.x += v
        if player == 1:
            if self.rect.left <= 0 or self.rect.right >= BORDER.left:
                self.rect.move_ip(-v,0)
        if player == 2:
            if self.rect.left <= BORDER.right or self.rect.right >= WIDTH:
                self.rect.move_ip(-v,0)
    
    def move_vertical(self,v):
        self.rect.move_ip(0,v)
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.rect.move_ip(0,-v)

red=Spaceship(RED_SPACESHIP_IMG,270,650,250)
yellow=Spaceship(YELLOW_SPACESHIP_IMG,90,250,250)
sprites=pygame.sprite.Group()
sprites.add(red)
sprites.add(yellow)

def draw_window():
        WIN.blit(SPACE, (0, 0))
        pygame.draw.rect(WIN, "BLACK", BORDER)
        red_health_text = FONT.render("Health: " + str(red_health), 1, "WHITE")
        yellow_health_text = FONT.render("Health: " + str(yellow_health), 1, "WHITE")
        WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        WIN.blit(yellow_health_text, (10, 10))

red_bullets=[]
yellow_bullets=[]

def draw_bullets():
    for bullet in red_bullets:
        pygame.draw.rect(WIN,"red",bullet)
        bullet.x -= BULLET_VEL
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,"yellow",bullet)
        bullet.x += BULLET_VEL

YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+1

def draw_winner(text):
    draw_text = FONT.render(text, 1, "WHITE")
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2,
                          HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

clock = pygame.time.Clock()

def handle_bullets():
    global red_health , yellow_health
    for bullet in yellow_bullets:
        if red.rect.colliderect(bullet):
            red_health-=1
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)        

    for bullet in red_bullets:
        if yellow.rect.colliderect(bullet):
            yellow_health-=1
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

    for bullet1 in red_bullets:
        for bullet2 in yellow_bullets:
            if bullet1.colliderect(bullet2):
                red_bullets.remove(bullet1)
                yellow_bullets.remove(bullet2)
    

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_LCTRL:
                bullet=pygame.Rect(yellow.rect.x + yellow.rect.width, yellow.rect.y + yellow.rect.height//2 - 2, 10, 5)
                yellow_bullets.append(bullet)
                BULLET_FIRE.play()

            if event.key == K_RCTRL:
                bullet=pygame.Rect(red.rect.x , red.rect.y + red.rect.height//2 - 2, 10, 5)
                red_bullets.append(bullet)
                BULLET_FIRE.play()
            
        if event.type == RED_HIT:
            red_health -= 1
            BULLET_HIT.play()


        if event.type == YELLOW_HIT:
            yellow_health -= 1
            BULLET_HIT.play()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_a]:
        yellow.move_horizontal(-vel,1)

    if keys_pressed[K_d]:
        yellow.move_horizontal(vel,1)

    if keys_pressed[K_w]:
        yellow.move_vertical(-vel)

    if keys_pressed[K_s]:
        yellow.move_vertical(vel)

    if keys_pressed[K_LEFT]:
        red.move_horizontal(-vel,2)

    if keys_pressed[K_RIGHT]:
        red.move_horizontal(vel,2)

    if keys_pressed[K_UP]:
        red.move_vertical(-vel)

    if keys_pressed[K_DOWN]:
        red.move_vertical(vel)

    draw_window()
    sprites.draw(WIN)
    draw_bullets()
    handle_bullets()

    if red_health <= 0:
        winner_text="YELLOW WINS"
        draw_winner(winner_text)

    if yellow_health <= 0:
        winner_text="RED WINS"
        draw_winner(winner_text)

    pygame.display.update()

pygame.quit()

    


    




        