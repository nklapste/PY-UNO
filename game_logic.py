
import card_logic
import display_funct
import game_control
import Main_Decision_Tree
import pygame

global winners
winners = []


def update_hatval(player, target, hate_increase=1):
    try:
        target.hatval[player] += hate_increase
    except KeyError:
        target.hatval[player] = hate_increase

def degrade_hatval(player):
    for hated_player in player.hatval.keys():
        if player.hatval[hated_player] > 0:
            player.hatval[hated_player] -= 1


def increment_card_old_vals(player):
    """
    Function for AI use that updates the old values of their hands cards.
    Each turn the all of the current turn AI's cards old values goes up by one.
    """
    for card in player.hand:
        card.old_val += 1


def compute_turn(players, turn, turn_iterator):
    """
    Function that handles PY-UNO turn iterations for any amount of players.
    """
    turn = turn + turn_iterator
    # catch to reloop overs players array
    if turn < 0:
        turn = len(players) - 1
    elif turn >= len(players):
        turn = 0
    print("Turn iterator: ", turn_iterator)
    print("Turn end \n\n")

    return turn


def check_update(board, allowed_card_list, selected, player, players, update):
    if update:
        update = False
        if selected is None:
            display_funct.redraw_screen(
                [(player, None)], board, players)
        else:
            display_funct.redraw_screen(
                [(player, allowed_card_list[selected])], board, players)
    return update


def add_winner(player):
    global winners
    print(player.name, "won and leaves this round!")
    winners.append(player)


def check_winners(player):
    global winners
    if player.hand == []:  # conditions for winning!
        print(player.name, "won and leaves this round!")
        winners.append(player)


def check_game_done(players):
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
                game_control.get_keypress(event)


def player_turn(board, deck, player, allowed_card_list, selected):
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

    args:
        board: a game_classes.py board class in which the cards within the game
        will be played on. The board class is used within some internal logic
        decisions and thus is needed.

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

        print("Turn number:", turn_tot)
        print("PLAYER: ", player.name, "TURN")

        if player.skip:
            print("skipping", player.name, "turn")
            player.skip = False
            if player.AI:
                increment_card_old_vals(player)

        elif player.AI:
            increment_card_old_vals(player)

            Main_Decision_Tree.travel_Main_Decision_Tree(board, deck, player,
                                                         players, player.Main_Decision_Tree.Dec_Tree)
            degrade_hatval(player)                                             

            if player in winners:  # TODO
                players.remove(player)
                print("removing player", player.name)
                check_game_done(players)
                turn = compute_turn(players, turn, board.turn_iterator)
                continue


            turn = compute_turn(players, turn, board.turn_iterator)

            continue
        else:
            turn_done = False
            selected = None
            skipping = False

            allowed_card_list = card_logic.card_allowed(board, player)
            print("allowed cards: ", allowed_card_list)

            display_funct.redraw_screen([(player, None)], board, players)

            while not turn_done:
                (update, selected, turn_done) = player_turn(
                    board, deck, player, allowed_card_list, selected)

                check_winners(player)


                update = check_update(board, allowed_card_list, selected,
                                      player, players, update)

            if not skipping:
                drop_again = card_logic.card_played_type(
                    board, deck, player, players)

            if player in winners:  # TODO
                players.remove(player)
                print("removing player", player.name)
                check_game_done(players)
                turn = compute_turn(players, turn, board.turn_iterator)
                continue

        # if the player plays a drop agian card dont iterate turn
        if drop_again:
            drop_again = False
            print(player.name, "Allowed to play another card, replaying!\n")
        else:
            turn = compute_turn(players, turn, board.turn_iterator)
            turn_tot += 1

########################################################
