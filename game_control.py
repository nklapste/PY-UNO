import pygame
import display_funct
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


########################################################
def select_move_color(select_L, select_R, selected):
    if selected is None:
        selected = 0
    if select_R:
        selected += 1
        if selected >= 4:  # catch
            selected = 3
            return selected
    elif select_L:
        selected -= 1
        if selected < 0:  # catch
            selected = 0
            return selected
    return selected


def player_LR_selection_color(selected=None):
    select_L = False
    select_R = False
    select_UP = False
    update = False
    turn_done = False
    if selected is None:
        selected = 0
    for event in pygame.event.get():
        (select_L, select_R, select_UP) = get_keypress(event)
    if select_R or select_L:  # if  keystoke to pick card was entered

        selectednew = select_move_color(select_L, select_R, selected)

        if selected == selectednew:
            pass
        else:
            selected = selectednew
            update = True

        select_L = False
        select_R = False

    if select_UP:  # if  keystoke to play card was entered
        update = True
        turn_done = True

    return (update, selected, turn_done)


def player_choice_color():
    '''
    Loop that waits for player input on choosing a color state for the board
    '''
    # setuop intial value of selected
    # and initially render the menu screen
    selected = None
    display_funct.redraw_screen_menu_color(None)
    while True:
        (update, selected, turn_done) = player_LR_selection_color(selected)
        if update:
            display_funct.redraw_screen_menu_color(selected)
        if turn_done:
            if selected == 0:
                print("choosing green")
                return "g"
            if selected == 1:
                print("choosing blue")
                return "b"
            if selected == 2:
                print("choosing yellow")
                return "y"
            if selected == 3:
                print("choosing red")
                return "r"
########################################################
def select_move_target(select_L, select_R, players, selected):
    if selected is None:
        selected = 0
    if select_R:
        selected += 1
        if selected >= len(players):  # catch
            selected = len(players) - 1
            return selected
    elif select_L:
        selected -= 1
        if selected < 0:  # catch
            selected = 0
            return selected
    return selected


def player_LR_selection_target(players, selected=None):
    select_L = False
    select_R = False
    select_UP = False
    update = False
    turn_done = False

    if selected is None:
        selected = 0
    for event in pygame.event.get():
        (select_L, select_R, select_UP) = get_keypress(event)
    if select_R or select_L:  # if  keystoke to pick card was entered
        selectednew = select_move_target(select_L, select_R, players, selected)

        if selected == selectednew:
            pass
        else:
            selected = selectednew
            update = True

        select_L = False
        select_R = False

    if select_UP:  # if  keystoke to play card was entered
        update = True
        turn_done = True

    return (update, selected, turn_done)


def player_choice_target(players):
    selected = None
    display_funct.redraw_screen_menu_target(players, None)
    while True:
        (update, selected, turn_done) = player_LR_selection_target(players, selected)
        if update:
            display_funct.redraw_screen_menu_target(players, selected)
        if turn_done:
            target = players[selected]
            return target
########################################################
