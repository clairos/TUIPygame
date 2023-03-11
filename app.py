import pygame
from sys import exit

pygame.init() 
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('te amo fernandinha', False, 'Black')

frog_surface = pygame.image.load('graphics/frog/frog1.png').convert_alpha()
frog_rectangle = frog_surface.get_rect(bottomright = (800, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (50, 300)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos): print('collision')

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (250, 50))

    frog_rectangle.x -= 3
    if frog_rectangle.right <= 0: frog_rectangle.left = 800
    screen.blit(frog_surface, frog_rectangle)
    screen.blit(player_surface, player_rectangle)

    # if player_rectangle.colliderect(frog_rectangle):
    #     ...

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos):
    #     ...

    pygame.display.update() 
    clock.tick(60)
