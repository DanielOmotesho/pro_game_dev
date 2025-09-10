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
