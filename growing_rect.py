# growing rectangle project

import pygame
pygame.init()       
screen= pygame.display.set_mode((600,600))
screen.fill((255,255,255))
blue = (0,0,255)
pygame.display.update()

class Rectangle():
    def __init__(self,color,pos,width,height,line_width):
        self.rect_color = color
        self.rect_pos = pos
        self.rect_width = width      
        self.rect_height = height
        self.rect_line_width = line_width
        self.rect_surface = screen
        
    def draw(self):
       pygame.draw.rect(self.rect_surface, self.rect_color, (self.rect_pos[0], self.rect_pos[1], self.rect_width, self.rect_height), self.rect_line_width)

    def grow(self,w,h):
        self.rect_width = self.rect_width + w
        self.rect_height = self.rect_height + h
        pygame.draw.rect(self.rect_surface, self.rect_color, (self.rect_pos[0], self.rect_pos[1], self.rect_width, self.rect_height), self.rect_line_width)
# instance of the class / object
rectangle = Rectangle(blue,(300,300),25,25,0)
rectangle.draw()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            rectangle.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            rectangle.grow(20,20) # important
            pygame.display.update()
            
        # if event.type == pygame.MOUSEMOTION:
        #     pos = pygame.mouse.get_pos()
        #     circle = Circle("yellow",(22,22),5,5)
        #     circle.draw()
        #     pygame.display.update()   
        
