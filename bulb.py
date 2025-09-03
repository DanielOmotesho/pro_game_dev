import pygame
import pgzrun
import time

WIDTH=700
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display("off_bulb.jpg")#wrong command

image=pygame.image.load("images/on_bulb.jpg")
img=pygame.transform.scale(image,(WIDTH,HEIGHT))


image2=pygame.image.load("images/off_bulb.jpg")
img2=pygame.transform.scale(image2,(WIDTH,HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            #pygame.display("on_bulb.jpg")#wrong command
            screen.blit(img2,(0,0))
            pygame.display.update()
            time.sleep(1)

        if event.type==pygame.MOUSEBUTTONUP:
            #pygame.display("off_bulb.jpg")#wrong command
            screen.blit(img,(0,0))
            pygame.display.update()
            time.sleep(1)