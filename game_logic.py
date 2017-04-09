
import card_logic
import display_funct
import game_control
import pygame


########################################################
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
    turn_iterator = 1
    turn = 0
    turn_tot = 0
    drop_again = False

    while True:

        for player in range(len(players)):
            player = players[turn]
            print("Turn number:", turn_tot)
            print("Players", turn + 1, "turn")
            print("PLAYER: ", player.name, "TURN")

            if player.skip:
                print("skipping", player.name, "turn")
                player.skip = False

            elif player.AI:
                pass
                #TODO INTERGRATE AI

            else:
                turn_done = False
                selected = None
                skipping = False

                allowed_card_list = card_logic.card_allowed(board, player)
                print("allowed cards: ", allowed_card_list)

                # if no cards can be played skip turn
                if allowed_card_list == []:
                    print("no playable cards, drawing and skipping")
                    player.grab_card(deck)
                    turn_done = True
                    skipping = True

                display_funct.redraw_screen([(player, None)], board, players)

                while not turn_done:
                    (update, selected, turn_done) = player_turn(
                        board, deck, player, allowed_card_list, selected)

                    if player.hand == []:  # conditions for winning!
                        print(str(player.name), "wins!!")
                        while 1:
                            for event in pygame.event.get():
                                game_control.get_keypress(event)

                    if update:
                        update = False
                        if selected is None:
                            display_funct.redraw_screen(
                                [(player, None)], board, players)
                        else:
                            display_funct.redraw_screen(
                                [(player, allowed_card_list[selected])], board, players)
                if not skipping:
                    (turn_iterator, drop_again) = card_logic.card_played_type(
                        board, deck, player, players, turn_iterator)

            # if the player plays a drop agian card dont iterate turn
            if drop_again:
                drop_again = False
                continue
            else:
                turn = turn + turn_iterator
                # catch to reloop overs players array
                if turn < 0:
                    turn = len(players) - 1
                elif turn >= len(players):
                    turn = 0
                print("Turn iterator: ", turn_iterator)
                print("Turn end \n\n")
                turn_tot += 1
########################################################
