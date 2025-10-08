import random
import pgzrun
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 900
screen_height = 963
screen = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont("Bauhaus 93", 60)
ground_scroll = 0
scroll_speed = 4
#initially bird starting pos
flying = False
game_over = False
pipe_gap = 150
pipe_frquency = 1500
#how many seconds have past since start of game - how frequently pipes appeared
last_pipe = pygame.time.get_ticks()-pipe_frquency
score = 0
pass_pipe = False

bg = pygame.image.load("images/background.png")
ground = pygame.image.load("images/ground.png")
restart = pygame.image.load("images/restart.png")

def draw_text(text, font, text_col, x, y):
    txt = font.render(text, True, text_col)
    screen.blit(txt, (x, y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    #placement of initial bird
    flappy.rect.y = int(screen_height / 2)
    score = 0
    return score
  
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            #if we are pressing dominant(0) key on mouse then the action will happen the restart button is pressed
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image,(self.rect.x,self.rect.y))
        #answer to something we have asked value of action will become true return also means end of function
        return action
    
button = Button(screen_width/2-50,screen_height/2-50,restart)     

