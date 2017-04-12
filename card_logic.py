import game_control
import game_logic

def update_mem_trees(board, deck, player, players):
    pass
    #TODO

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

    O(n) runtime where n is the number of cards in the players hand
    """
    i = 0
    allowed = []

    for card in player.hand:   # O(n)
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
    Card function that handles when the player plays a wild pick 4 card.

    Starts subfunctions that handel player color choice, and player target
    choice. This function then prints out the results of the players decisions
    on the game.

    O(n) runtime
    """
    board.color = game_control.player_choice_color()  # O(1)
    print("New color: ", board.color)
    players_temp = players[:]  # O(n)
    players_temp.remove(player)  # O(n)
    target = game_control.player_choice_target(players_temp)  # O(n)
    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 4)
    print("Trageted players hand size after: ", len(target.hand))
    # update targets hatval of player
    game_logic.update_hatval(player, target, 4)


def wild_color(board, deck, player):
    """
    Card function that handles when the player plays a wild color card.

    This makes the game move onto making the player choose a color.This
    chosen color updates the current board color. After a color has been
    chosen the player then can play another card of the same color.

    O(1) runtime
    """
    board.color = game_control.player_choice_color()  # O(1)
    print("New color: ", board.color)


def draw_2(board, deck, player, players):
    """
    Card function that handles when the player plays a draw 2 card.

    This makes the game move to the target selection menu. After a target is
    selected the targeted player is then forced to draw 2 cards.

    O(n) runtime
    """
    players_temp = players[:]
    players_temp.remove(player)
    target = game_control.player_choice_target(players_temp)   # O(n)
    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 2)
    print("Trageted players hand size after: ", len(target.hand))
    # update targets hatval of player
    game_logic.update_hatval(player, target, 2)


def skip(board, deck, player, players):
    """
    Card function that handles when the player plays a skip turn card.

    This makes the game move to the target selection menu. After a target is
    selected the targeted player is then forced skip their next turn.

    O(n) runtime
    """
    players_temp = players[:]
    players_temp.remove(player)
    target = game_control.player_choice_target(players_temp)  # O(n)
    print("Targeted player skipping: ", target.name)
    target.skip = True
    # update targets hatval of player
    game_logic.update_hatval(player, target, 1)


def reverse(board):
    """
    Card function that handles when the player plays the reverse card.

    Prints the original turn_iterator and then swaps sign of the
    original turn_iterator.

    Args: board class of a pyuno game in which its turn_iterator value will be
    accessed (should be 1 or -1)

    O(1) runtime
    """
    turn_iterator = board.turn_iterator
    print("reversing", turn_iterator)
    board.turn_iterator = -turn_iterator
########################################################


def card_played_type(board, deck, player, players):
    """
    Logic function that takes the most recently played card and decides
    what game actions are needed to be taken to accomadate. These actions are
    then preformed by other functions detailed above.

    O(n) runtime
    """
    if board.card_stack == []:  # catch for empty board
        return turn_iterator

    drop_again = False
    played_type = board.type
    played_color = board.color

    print("played", played_color, played_type, "by:", player.name)

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
        reverse(board)
        return False
    elif played_type.isdigit():     # normal number card played
        pass
    return drop_again
