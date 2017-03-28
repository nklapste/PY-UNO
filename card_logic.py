import game_control
import pygame
import display_funct


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
        (select_L, select_R, select_UP) = game_control.get_keypress(event)
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
        (select_L, select_R, select_UP) = game_control.get_keypress(event)
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

########################################################


def wild_pick_4(board, deck, player, players):
    board.color = player_choice_color()
    print("New color: ", board.color)

    players_temp = players[:]
    players_temp.remove(player)
    target = player_choice_target(players_temp)

    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 4)
    print("Trageted players hand size after: ", len(target.hand))


def wild_color(board, deck, player):
    board.color = player_choice_color()
    print("New color: ", board.color)


def draw_2(board, deck, player, players):
    players_temp = players[:]
    players_temp.remove(player)
    target = player_choice_target(players_temp)

    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 2)
    print("Trageted players hand size after: ", len(target.hand))


def skip(board, deck, player, players):
    players_temp = players[:]
    players_temp.remove(player)
    target = player_choice_target(players_temp)

    print("Choosing player: ", player.name)
    print("Targeted player skipping: ", target.name)
    target.skip = True


def reverse(turn_iterator):
    print("reversing", turn_iterator)
    return -turn_iterator
########################################################


def card_played_type(board, deck, player, players, turn_iterator):
    '''
    Logic function that takes the most recently played card and decides
    what game actions are needed to be taken to accomadate. These actions are
    then preformed by other functions detailed above.
    '''
    if board.card_stack == []:  # catch for empty board
        return turn_iterator

    drop_again = False
    played_type = board.type
    played_color = board.color

    print("played by: ", player.name)
    print("played card type: ", played_type)
    print("played card color: ", played_color)

    if played_color == "w":
        drop_again = True
        if played_type == "d":      # wild choose color draw 4 card played
            wild_pick_4(board, deck, player, players)
        elif played_type == "c":    # wild choose color card played
            wild_color(board, deck, player)
    elif played_type == "p":        # draw 2 card played
        draw_2(board, deck, player, players)
    elif played_type == "s":        # skip turn card played
        skip(board, deck, player, players)
    elif played_type == "r":        # reverse turns card played
        return (reverse(turn_iterator), False)
    elif played_type.isdigit():     # normal number card played
        pass
    return (turn_iterator, drop_again)
