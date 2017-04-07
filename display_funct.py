import game_classes
import pygame


# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)


# defining screen
size = width, height = 1500, 900
speed = [2, 2]
screen = pygame.display.set_mode(size)
screen.fill(black)


# default card rectangle size and card size
card_width = 130
card_height = 182
def_rect = pygame.Rect(0, 0, card_width, card_height)
face_down_card = game_classes.Card(
    "face_down", "small_cards/card_back.png", None)


def draw_top_stack_card(board):
    """
    Renders the top card of the card_stack on the board
    """
    # clear specific part of screen
    pygame.draw.rect(screen, black, ((width - card_width) // 2,
                                     (height - card_height) // 2, card_width, card_height), 0)

    if board.card_stack != []:
        top_card = board.card_stack[-1]
        top_card.rect = def_rect
        top_card.rect = top_card.rect.move(
            (width - card_width) // 2, (height - card_height) // 2)
        screen.blit(top_card.card_data, top_card.rect)
        pygame.display.flip()


def redraw_hand_visble(player, selected=None):
    """
    Redraws a players hand to be face up
    """
    # clear specific part of screen
    pygame.draw.rect(screen, black, (0, 600, width, 300), 0)


    # player playing placeholder graphic
    player_num = str(player.name[7])
    card_disp = game_classes.Card(
        "red", "small_cards/red_" + player_num + ".png", None)
    card_disp.rect = card_disp.rect.move(0, 900-card_height)


    # get a "middle" start postion for bliting cards
    start_pos = (width - 100 * len(player.hand)) // 2
    i = 0
    for card in player.hand:
        card.rect = def_rect
        if i == selected:
            card.rect = card.rect.move(start_pos, 600)
        else:
            card.rect = card.rect.move(start_pos, 700)
        card.rect = card.rect.move(100 * i, 0)
        screen.blit(card.card_data, card.rect)
        i += 1
    # displaying the placeholder playing player number
    screen.blit(card_disp.card_data, card_disp.rect)
    pygame.display.flip()

def redraw_hand_nonvisble(player, start_pos_horz, start_pos_vert=0):
    """
    redraws a players hand to be non visible
    """

    #placeholder player num graphics
    player_num = str(player.name[7])
    card_disp = game_classes.Card(
        "red", "small_cards/red_" + player_num + ".png", None)
    card_disp.rect = card_disp.rect.move(start_pos_horz, start_pos_vert)

    i = 0
    for card in player.hand:
        card.rect = def_rect
        card.rect = card.rect.move(start_pos_horz, start_pos_vert)
        card.rect = card.rect.move(80 * i, 0)
        screen.blit(face_down_card.card_data, card.rect)
        i += 1
    # displaying the placeholder player num graphics
    screen.blit(card_disp.card_data, card_disp.rect)
    pygame.display.flip()


def redraw_screen(player_you, board, players_other):
    """
    Redraws the screen to its "normal" state, where it renders the current
    players hand face up, the current card selected is raised, the most recently
    played card on the board face up, and other players' hands face down.
    """
    # # clear screen
    # screen.fill(black)

    # draw personal players hand
    for player in player_you:
        (player_dat, selected) = player
        redraw_hand_visble(player_dat, selected)

    players_temp = players_other[:]
    players_temp.remove(player_dat)
    # clear specific part of screen
    pygame.draw.rect(screen, black, (0, 0, width, 600), 0)
    # draw all active other hands in nice other places in the screen
    start_pos_horz = 0
    start_pos_vert = 0
    player_counts = 0
    for player in players_temp:
        hand_size = (80 * len(player.hand)) + (card_width - 80)
        if player_counts > 1:
            start_pos_vert = start_pos_vert + card_height + 20
            start_pos_horz = 0
            player_counts = 0
        print(player.name)
        print(start_pos_horz, start_pos_vert)
        redraw_hand_nonvisble(player, start_pos_horz, start_pos_vert)
        start_pos_horz = width - hand_size
        player_counts += 1

    # draw the top card on the board
    draw_top_stack_card(board)


def redraw_screen_menu_color(selected=None):
    # # clear screen
    pygame.draw.rect(screen, black, (0, 0, width, 600), 0)

    # get a "middle" start postion for bliting cards
    start_pos = ((width) // 2) - ((300 * 2 + card_width) // 2)
    # placeholders for color slection graphics
    card_g = game_classes.Card("green", "small_cards/green_0.png", None)
    card_b = game_classes.Card("blue", "small_cards/blue_0.png", None)
    card_y = game_classes.Card("yellow", "small_cards/yellow_0.png", None)
    card_r = game_classes.Card("red", "small_cards/red_0.png", None)

    color_array = [card_g, card_b, card_y, card_r]
    i = 0
    for card_c in color_array:
        card_c.rect = def_rect
        if i == selected:
            card_c.rect = card_c.rect.move(start_pos, 200)
        else:
            card_c.rect = card_c.rect.move(start_pos, 300)

        card_c.rect = card_c.rect.move(200 * i, 0)
        screen.blit(card_c.card_data, card_c.rect)

        i += 1
    pygame.display.flip()

def redraw_screen_menu_target(players, selected=None):
    # clear screen
    # screen.fill(black)

    # # clear screen (top half)
    pygame.draw.rect(screen, black, (0, 0, width, 600), 0)

    # get a "middle" start postion for bliting cards
    # start_pos=(width - 200 * len(players)) // 2
    start_pos = ((width) // 2) - (200 * (len(players) - 1) + card_width) // 2
    i = 0
    for player in players:
        player_num = str(player.name[7])
        card_disp = game_classes.Card(
            "red", "small_cards/red_" + player_num + ".png", None)
        card_disp.rect = def_rect
        if i == selected:
            card_disp.rect = card_disp.rect.move(start_pos, 200)
        else:
            card_disp.rect = card_disp.rect.move(start_pos, 300)
        card_disp.rect = card_disp.rect.move(200 * i, 0)
        screen.blit(card_disp.card_data, card_disp.rect)
        i += 1
    pygame.display.flip()
