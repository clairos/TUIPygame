import pygame
from sys import exit

pygame.init() # initialize pygame
screen = pygame.display.set_mode((800, 400)) # create the screen
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # font type, font size

# test_surface = pygame.Surface((100, 200)) # width, height
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black') # text, AA, color

while True: # runs forever
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN, JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP, JOYBUTTONDOWN, VIDEORESIZE, VIDEOEXPOSE, USEREVENT
            pygame.quit()
            exit()

    # draw all our elements
    # screen.blit(test_surface, (200, 100))
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (340, 50))

    # update everything
    pygame.display.update() # updates the 'screen' display surface
    clock.tick(60)
