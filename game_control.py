import display_funct
import os
import pygame


def get_keypress(event):
    """
    Main call function that grabs keypress events and returns logic values
    related to such keypresses.

    Note: if the QUIT event happens os._exit is called in which the entire
    PY-GAME instance is shutdown.

    O(1) runtime
    """
    select_L = False
    select_R = False
    select_UP = False

    if event.type == pygame.QUIT:
        os._exit(0)  # hard exit the program
    elif event.type == pygame.VIDEORESIZE:
        display_funct.handle_resize(event) # O(1)
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
    """
    O(1) runtime
    """
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
    """
    O(1) runtime
    """
    select_L = False
    select_R = False
    select_UP = False
    update = False
    turn_done = False
    if selected is None:
        selected = 0
    for event in pygame.event.get():  # O(1)
        (select_L, select_R, select_UP) = get_keypress(event)  # O(1)
    if select_R or select_L:  # if  keystoke to pick card was entered

        selectednew = select_move_color(select_L, select_R, selected)  # O(1)

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
    """
    Loop that waits for player input on choosing a color state for the board

    O(1) runtime (excluding loop) (assuming slection is made instantly)
    """
    # setuop intial value of selected
    # and initially render the menu screen
    selected = None
    display_funct.redraw_screen_menu_color(None)  # O(4)
    while True:
        (update, selected, turn_done) = player_LR_selection_color(selected) # O(1)
        if update:
            display_funct.redraw_screen_menu_color(selected)  # O(4) ==> O(1)
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
    """
    O(1) runtime
    """
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
    """
    O(1) runtime
    """
    select_L = False
    select_R = False
    select_UP = False
    update = False
    turn_done = False

    if selected is None:
        selected = 0
    for event in pygame.event.get():  # O(1)
        (select_L, select_R, select_UP) = get_keypress(event)  # O(1)
    if select_R or select_L:  # if  keystoke to pick card was entered
        selectednew = select_move_target(select_L, select_R, players, selected)  # O(1)

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
    """
    O(n) runtime where in is the length of players (assuming selection is made
    instantly)
    """
    selected = None
    display_funct.redraw_screen_menu_target(players, None) # O(n)
    while True:
        (update, selected, turn_done) = player_LR_selection_target(players,
                                                                   selected) # O(1)
        if update:
            display_funct.redraw_screen_menu_target(players, selected) # O(n)
        if turn_done:
            target = players[selected]
            return target
########################################################


def select_choose(player, board, selected=0):
    """
    O(1) runtime
    """
    player.play_card(board, selected)
    selected = None
    return selected


def select_move_hand(select_L, select_R, allowed_card_list, selected):
    """
    O(1) runtime
    """
    if selected is None:
        selected = 0
    if select_R:
        selected += 1
        if selected >= len(allowed_card_list):  # catch
            selected = len(allowed_card_list) - 1
            return selected
    elif select_L:
        selected -= 1
        if selected < 0:  # catch
            selected = 0
            return selected
    return selected


def player_LR_selection_hand(player, selected, board=None, allowed_card_list=None):
    '''
    Function that is a modification of player_LR_selection that decides the
    card the player is hovering over, additionally if the player selects the
    card they are hovering over; turn_done will be turned to true allowing for
    further progress within outside functions.

    O(1) runtime
    '''
    select_L = False
    select_R = False
    select_UP = False
    update = False
    turn_done = False

    for event in pygame.event.get(): # O(1)
        (select_L, select_R, select_UP) = get_keypress(event) # O(1)

    if select_R or select_L:  # if  keystoke to pick card was entered

        selectednew = select_move_hand(
            select_L, select_R, allowed_card_list, selected) # O(1)

        if selected == selectednew:
            pass
        else:
            selected = selectednew
            update = True

        select_L = False
        select_R = False

    elif select_UP:  # if  keystoke to play card was entered
        # catch for index nonetype error in allowed_card_list
        if selected is None:
            selected = 0

        selected = select_choose(player, board, allowed_card_list[selected]) # O(1)
        update = True
        turn_done = True

    return (update, selected, turn_done)
########################################################
