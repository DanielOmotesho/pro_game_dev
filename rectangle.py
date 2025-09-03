#import the module 
import pygame

# initialize pygame 
pygame.init()

#set dimensions of the screen
screen= pygame.display.set_mode((600,600))

#Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#screen fil
screen.fill(white)


#creating a Rectangle class
class Rect():
    # constructor - features
    def __init__(self,color,dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions=dimensions
        
    # functions 
    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

#creating Instances/ objects 

greenRect=Rect(green,(50,20,100,100))
redRect=Rect(red,(150,200,150,150))
blueRect=Rect(blue,(300,400,200,200))

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #accessing methods to draw rectangles 
    greenRect.draw()
    blueRect.draw()
    redRect.draw()


    #Display update to reflect the things on screeen
    pygame.display.update()

# quit pygame
pygame.quit()


# import pygame
# pygame.init()

# # Set dimensions of the screen
# screen = pygame.display.set_mode((600, 600))

# # Colors
# black = (0, 0, 0)
# white = (255, 255, 255)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)

# # Screen fill
# screen.fill(white)
# pygame.display.update()

# # Creating a Rectangle class
# class Rect():
#     def __init__(self, color, dimensions):
#         self.rect_surf = screen
#         self.rect_color = color
#         self.rect_dimensions = dimensions
        
# def draw(self):
#         self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

# # Creating instances
# greenRect = Rect(green, (50, 20, 100, 100))
# redRect = Rect(red, (150, 200, 150, 150))
# blueRect = Rect(blue, (300, 400, 200, 200))

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Draw rectangles
#     greenRect.draw()
#     blueRect.draw()
#     redRect.draw()

#     # Display update to reflect the things on screen
#     pygame.display.update()

# # Quit pygame
# pygame.quit()