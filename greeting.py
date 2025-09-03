import pygame
import time

pygame.init()
WIDTH=750
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("greeting")
image=pygame.image.load("images/greeting1.jpg")
img=pygame.transform.scale(image,(WIDTH,HEIGHT))

image2=pygame.image.load("images/greeting2.jpg")
img2=pygame.transform.scale(image2,(WIDTH,HEIGHT))

image3=pygame.image.load("images/greeting3.jpg")
img3=pygame.transform.scale(image3,(WIDTH,HEIGHT))



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    font=pygame.font.SysFont("Arial",70)
    text=font.render("HAPPY BIRTHDAY TO YOU",True,"black")
    
    screen.blit(img,(0,0))
    screen.blit(text,(30,350))
    pygame.display.update()
    time.sleep(2)
 
    font2=pygame.font.SysFont("Georgia",70)
    text2=font2.render("God bless you",True,"black")

    font3=pygame.font.SysFont("CanvaSans",70)
    text3=font3.render("have a good one",True,"black")

    screen.blit(img2,(0,0))
    screen.blit(text2,(0,0))
    pygame.display.update()
    time.sleep(2)

    screen.blit(img3,(0,0))
    screen.blit(text3,(0,0))
    pygame.display.update()
    time.sleep(2)

    

