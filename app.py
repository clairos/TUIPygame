import pygame
from sys import exit

pygame.init() # initialize pygame
screen = pygame.display.set_mode((800, 400)) # create the screen
pygame.display.set_caption('Runner')

while True: # runs forever
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN, JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP, JOYBUTTONDOWN, VIDEORESIZE, VIDEOEXPOSE, USEREVENT
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    pygame.display.update() # updates the 'screen' display surface
