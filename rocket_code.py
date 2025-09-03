import pygame
from pygame.locals import *
import time

pygame.init()
pygame.font.init()
WIDTH=700
HEIGHT=650
screen=pygame.display.set_mode((WIDTH,HEIGHT))

player_x=(350)
player_y=(250)
keys=[False,False,False,False]

player = pygame.image.load("images/rocket.png")
background = pygame.image.load("images/bg2.png")

font = pygame.font.SysFont("CanvaSans",30)

while player_y<650:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            
            if event.key==K_LEFT:
                keys[1]=True

            if event.key==K_DOWN:
                keys[2]=True

            if event.key==K_RIGHT:
                keys[3]=True
            
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False

            if event.key==K_LEFT:
                keys[1]=False

            if event.key==K_DOWN:
                keys[2]=False

            if event.key==K_RIGHT:
                keys[3]=False
            
    if keys[0]:
        if player_y>0:
            player_y -= 5
    
    if keys[2]:
        if player_y<630:
            player_y += 5

    if keys[1]:
        if player_x>0:
            player_x -= 5

    if keys[3]:
        if player_x<670:
            player_x += 5
    
    player_y+=0.5

text=font.render("GAME 0VER",True,"white")
screen.blit(text,(WIDTH/2,HEIGHT/2))
pygame.display.update()
time.sleep(2)

pygame.quit()



