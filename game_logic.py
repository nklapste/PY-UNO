
import card_logic
import display_funct
import game_control
import Main_Decision_Tree
import pygame

# global list containing the winners in placement order
global winners
winners = []


def update_hatval(player, target, hate_increase=1):
    """
    Function that updates the hatval of a player in refrence to a player.

    Eg: a player (player A) plays a skip turn card on a target (player B)
    thus player B's hatval of player A goes up. The higher the hatval the
    more likely that player B will prioritize targeting player A over other
    logical plays.

    O(1) runtime
    """
    try:
        target.hatval[player] += hate_increase
    except KeyError:
        target.hatval[player] = hate_increase


def degrade_hatval(player):
    """
    Funciton that de-iterates the current players hatval of all other players
    by 1. Essentially preventing hatevals going extremely high, and making very
    mean AIs.

    O(n) runtime where n is the number of hated players number of
    (keys of players hatval).
    """
    for hated_player in player.hatval.keys():
        if player.hatval[hated_player] > 0:
            player.hatval[hated_player] -= 1


def increment_card_old_vals(player):
    """
    Function for AI use that updates the old values of their hands cards.
    Each turn the all of the current turn AI's cards old values goes up by one.

    O(n) runtime where n is the size of the players hand
    """
    for card in player.hand:
        card.old_val += 1


def compute_turn(players, turn, turn_iterator):
    """
    Function that handles PY-UNO turn iterations for any amount of players.

    O(1) runtime
    """
    turn = turn + turn_iterator
    # catch to reloop over players array
    if turn < 0:
        turn = len(players) - 1
    elif turn >= len(players):
        turn = 0
    print("Turn iterator: ", turn_iterator)
    print("__TURN_END__ \n")

    return turn


def check_update(board, allowed_card_list, selected, player, players, update):
    """
    Checks to see during a human players turn if updating the screen is
    nessicarry. This helps reduce redundant updates and keeps the screen
    refreshing crisp.

    Worst case:
    O(m*n) runtime where m is the amount of players to be drawn and
    n is the size of the players hand. Since both of these sizes should be
    relatively small optimizing was considered negligible.
    """
    if update:
        update = False
        if selected is None:
            display_funct.redraw_screen(
                [(player, None)], board, players)
        else:
            display_funct.redraw_screen(
                [(player, allowed_card_list[selected])], board, players)
    return update


def check_winners(player):
    """
    Checks to see if a player has met the conditions of winning a round
    (having no more cards in hand). If so the player is appened onto the global
    list winners.

    O(1) runtime
    """
    global winners
    if player.hand == []:  # conditions for winning!
        print(player.name, "won and leaves this round!")
        winners.append(player)


def check_game_done(players):
    """
    Checks to see if the PY-UNO game is over (only one player left with cards).
    If so the last player with cards is appened to the winners list and then
    the game displays the winners with placeholder green cards (with a numeric
    value the same as their name number) in win order. The left most card
    displayed is first place while the rightmost is last. Winners are also
    printed out within terminal (printed in winning placement order).

    Args:
        players: a game_classes.py player that will iterate through allowing
        for turns with each player.

    O(n) runtime where n is the length of winners. However this is the end game
    state so this is likely no a problem.
    """
    global winners

    if len(players) <= 1:
        print("\n\ngame done!!!!!")
        # adding last place
        winners.append(players[0])

        place = 1
        print("displaying winners in order:")
        for player in winners:
            print(place, player.name)
            place += 1

        display_funct.draw_winners(winners)

        while 1:  # wait till the player exits out of the game
            for event in pygame.event.get():
                (select_L, select_R, select_UP) = game_control.get_keypress(event)

                if select_UP:
                    # clear winners for next game
                    winners = []
                    return True

    return False


def extern_AI_player_turn(board, deck, player, players, turn):
    increment_card_old_vals(player)  # O(n)

    Main_Decision_Tree.travel_Main_Decision_Tree(board, deck, player,
                                                 players, player.Main_Decision_Tree.Dec_Tree)
    degrade_hatval(player)  # O(n)


def extern_player_turn(board, deck, player, players, turn):
    drop_again = True
    while drop_again:
        turn_done = False
        selected = None

        # redraw display at start of human turn
        display_funct.redraw_screen([(player, None)], board, players)

        # grab the list of allowed_cards cards
        allowed_card_list = card_logic.card_allowed(board, player)
        # if no cards can be played end turn
        if len(allowed_card_list) == 0:
            print("no playable cards skipping and drawing\n\n")
            player.grab_card(deck)
            turn = compute_turn(players, turn, board.turn_iterator)
            return (player, turn)

        while not turn_done:
            (update, selected, turn_done) = intern_player_turn(
                board, deck, player, allowed_card_list, selected)

            check_winners(player)

            update = check_update(board, allowed_card_list, selected,
                                  player, players, update)

        # returns false unless a drop_again type card is played
        drop_again = card_logic.card_played_type(board, deck,
                                                 player, players)

    return (player, turn)


def intern_player_turn(board, deck, player, allowed_card_list, selected):
    update = False
    if allowed_card_list == []:
        player.grab_card(deck)
        selected = None
        update = True
        turn_done = True
        return (update, selected, turn_done)

    while not update:
        (update, selected, turn_done) = game_control.player_LR_selection_hand(
            player, selected, board, allowed_card_list)

    return (update, selected, turn_done)


def game_loop(board, deck, players):
    """
    Main logic and turn while loop that controlls the game.

    Args:
        board: a game_classes.py board class in which the cards within the game
        will be played on.

        deck: a game_classes.py deck class to be used as the deck to have cards
        drawn from.

        players: a game_classes.py player that will iterate through allowing
        for turns with each player.
    """
    board.turn_iterator = 1
    turn = 0
    turn_tot = 0
    drop_again = False

    while True:
        player = players[turn]
        turn_tot += 1
        print("Turn number:", turn_tot)
        print("PLAYER: ", player.name, "TURN")

        if player.skip:
            if player.AI:
                increment_card_old_vals(player)

            print("skipping", player.name, "turn")
            player.skip = False

        elif player.AI:  # handle for an AI player
            extern_AI_player_turn(board, deck, player, players, turn)

        else:            # handle for a human player
            (update, turn_done) = extern_player_turn(board, deck,
                                                     player, players, turn)

        # check if the player won this round and properly remove them from the
        # game. Also check if the game is done "only one player left".
        if player in winners:
            players.remove(player)
            restart_bool = check_game_done(players)

            # leaves this instance of the game logic loop back to PY-UNO start
            # in which a new game is started
            if restart_bool:
                return

        # iterate the turn
        turn = compute_turn(players, turn, board.turn_iterator)
