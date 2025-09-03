import pgzrun
import pygame

WIDTH=800
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))


class Circle():
    def __init__(self,pos,radius,clr):
        self.pos=pos
        self.radius=radius
        self.clr=clr
        self.surface=screen

    def draw(self):
        pygame.draw.circle(self.surface,self.clr,self.pos,self.radius)
    def grow(self,r):
        self.radius=self.radius+r
        pygame.draw.circle(self.surface,self.clr,self.pos,self.radius)

circle= Circle((400,400),25,"green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            circle.draw()
            pygame.display.update()

        if event.type==pygame.MOUSEBUTTONUP:
            circle.grow(10)
            pygame.display.update()







  