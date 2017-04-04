import game_control
import pygame
import display_funct


def card_allowed(board, player):
    """
    Args:
        player: a pyuno Player class in which their hand is being evaluated
                wether it has valid cards to play or not.
        board: a pyuno Board class in which its current stat is the determining
               factor wether a players card is valid or not.
    Returns:
        allowed: a list of cards allowed to be played from a certain players
                 hand.
    """
    i = 0
    allowed = []

    for card in player.hand:
        if board.card_stack == [] or board.color == "w":
            allowed = range(len(player.hand))
            return allowed
        if card.color == "w":
            allowed.append(i)
        elif card.type == board.type or card.color == board.color:
            allowed.append(i)
        i += 1
    return allowed


########################################################
def wild_pick_4(board, deck, player, players):
    """
    Function that handles when the player plays a wild pick 4 card, going to
    subfunctions that handel player color choice, and player target choice.
    This function then prints out the results of the players decisions on the
    game.
    """
    board.color = game_control.player_choice_color()
    print("New color: ", board.color)
    players_temp = players[:]
    players_temp.remove(player)
    target = game_control.player_choice_target(players_temp)
    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 4)
    print("Trageted players hand size after: ", len(target.hand))


def wild_color(board, deck, player):
    board.color = game_control.player_choice_color()
    print("New color: ", board.color)


def draw_2(board, deck, player, players):
    players_temp = players[:]
    players_temp.remove(player)
    target = game_control.player_choice_target(players_temp)
    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 2)
    print("Trageted players hand size after: ", len(target.hand))


def skip(board, deck, player, players):
    players_temp = players[:]
    players_temp.remove(player)
    target = game_control.player_choice_target(players_temp)
    print("Targeted player skipping: ", target.name)
    target.skip = True


def reverse(turn_iterator):
    """
    Function that handles when the player plays the reverse card.
    Prints the original turn_iterator and then returns the negitive of the
    original turn_iterator.

    Args: turn_iterator of a pyuno game (should be 1 or -1)

    Returns: Negitive of turn_iterator
    """
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
