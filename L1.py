#OOPS
import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))



class Boxes():
    #properties-constructor
    def __init__(self,dimensions,color):
        self.surf = screen
        self.dimensions = dimensions
        self.color = color
       

    #functions
    def draw (self):
        self.rect = pygame.draw.rect(self.surf, self.dimensions, self.color)
    
#OBJECT
red = Boxes((100,100,50,50),"red")


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    red.draw()
    pygame.display.update()
pygame.quit()
