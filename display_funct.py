import game_classes
import pygame

# defining screen
size = width, height = 900, 900
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
screen.fill(black)

# default card rectangle size
def_rect = pygame.Rect(0, 0, 130, 182)
face_down_card = game_classes.Card(
    "face_down", "small_cards/card_back.png", None)


def draw_top_stack_card(board):
    """
    Renders the top card of the card_stack on the board
    """
    if board.card_stack != []:
        top_card = board.card_stack[-1]
        top_card.rect = def_rect
        top_card.rect = top_card.rect.move(
            (width - 130) // 2, (height - 182) // 2)
        screen.blit(top_card.card_data, top_card.rect)
        pygame.display.flip()


def redraw_hand_visble(player, selected=None):
    """
    Redraws a players hand to be face up
    """
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
        pygame.display.flip()
        i += 1


def redraw_hand_nonvisble(player, selected=None):
    """
    redraws a players hand to be non visible
    """

    # get a "middle" start postion for bliting cards
    start_pos = (width - 100 * len(player.hand)) // 2
    i = 0
    for card in player.hand:
        card.rect = def_rect
        if i == selected:
            card.rect = card.rect.move(start_pos, 100)
        else:
            card.rect = card.rect.move(start_pos, 0)

        card.rect = card.rect.move(100 * i, 0)
        screen.blit(face_down_card.card_data, card.rect)
        pygame.display.flip()
        i += 1


def redraw_screen(player_you, board, player_other):
    """
    Redraws the screen to its "normal" state, where it renders the current
    players hand face up, the current card selected is raised, the most recently
    played card on the board face up, and other players' hands face down.
    """
    # clear screen
    screen.fill(black)

    # draw personal players hand
    for player in player_you:
        (player_dat, selected) = player
        redraw_hand_visble(player_dat, selected)

    # draw all active other hands
    for player in player_other:
        redraw_hand_nonvisble(player)

    # draw the top card on the board
    draw_top_stack_card(board)


def redraw_screen_menu_color(selected=None):
    # clear screen
    screen.fill(black)
    # get a "middle" start postion for bliting cards
    start_pos = ((width - 400) // 2) - 300
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
        pygame.display.flip()
        i += 1


def redraw_screen_menu_target(players, selected=None):
    # clear screen
    screen.fill(black)
    # get a "middle" start postion for bliting cards
    start_pos = (width - 100 * len(players)) // 2
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
        pygame.display.flip()
        i += 1
