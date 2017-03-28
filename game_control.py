import pygame
import os

def get_keypress(event):
    select_L = False
    select_R = False
    select_UP = False

    if event.type == pygame.QUIT:
        os._exit(0) # hard exit the program
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            select_L = True

        elif event.key == pygame.K_RIGHT:
            select_R = True

        elif event.key == pygame.K_UP:
            select_UP = True

    return (select_L, select_R, select_UP)
