import os
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))

def handle_resize():
        screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        # screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))

        pygame.display.flip()
