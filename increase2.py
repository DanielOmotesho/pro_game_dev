import pgzrun
import pygame

WIDTH=800
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
blue=(0,0,255)

class Rect():
    def __init__(self,pos,dimensions,clr):
       self.pos=pos
       self.dimensions=dimensions
       self.clr=clr
       self.surface=screen

    def draw(self):
        self.rect = pygame.draw.rect(self.surface,self.pos,self.dimensions,self.clr)
    def grow(self,r):
        self.dimensions=self.dimensions + r
        self.rect = pygame.draw.rect(self.surface,self.pos,self.dimensions,self.clr)

#circle= Circle((400,400),25,"green")

rectangle= Rect((40,40),(100,100,50,50),blue)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            rectangle.draw()
            pygame.display.update()

        if event.type==pygame.MOUSEBUTTONUP:
            rectangle.grow(10)
            pygame.display.update()

            #code was not working (ask teacher during lesson)
