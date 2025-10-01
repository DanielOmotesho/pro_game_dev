import pygame
pygame.init()
WIDTH=800
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")
pygame.display.update()

ludo = pygame.image.load("images/ludo.png")
temple_run = pygame.image.load("images/temple_run.png")
candy_crush = pygame.image.load("images/candy_crush.jpg")
subway_surfers = pygame.image.load("images/subway_surfers.png")

screen.blit(ludo,(150,100))
screen.blit(temple_run,(150,150))
screen.blit(candy_crush,(150,200))
screen.blit(subway_surfers,(150,250))

font = pygame.font.SysFont("Times New Roman",50)
ludo_text = font.render("LUDO",True,"black")
templerun_text = font.render("TEMPLE RUN ",True,"black")
candy_crush_text = font.render("CANDY CRUSH ",True,"black")
subway_surfers_text = font.render("SUBWAY SURFERS ",True,"black")

screen.blit(ludo_text,(500,100))
screen.blit(templerun_text,(500,150))
screen.blit(candy_crush_text,(500,200))
screen.blit(subway_surfers_text,(500,250))

pygame.display.update()

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pyagme.K_ESCAPE:
                pygame.quit()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,"red",(pos),15,0)
        pygame.display.update()

    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,"black",pos,pos2,5)
        pygame.draw.circle(screen,"red",(pos2),15,0)
        pygame.display.update()
        

        







