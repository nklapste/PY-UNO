#!/usr/bin/python
# -*- coding: utf-8 -*-

"""argparse entrypoint script"""

import argparse
import sys


def get_parser() -> argparse.ArgumentParser:
    """Create and return the argparser for trivector"""
    parser = argparse.ArgumentParser(
        description=""
    )
    return parser


def main(argv=sys.argv[1:]):
    """argparse function"""
    parser = get_parser()
    args = parser.parse_args(argv)

    return 0


if __name__ == "__main__":
    sys.exit(main())



# TODO
from pyuno.deck import gen_rand_deck
from pyuno import game_classes, game_AI, game_logic, display

# loop for allowing multiple games to be restarted
while True:
    # initializing the board to be used within the game
    board1 = game_classes.Board("board1")

    # initializing a deck to be used within the game (3 copies are added to
    # each other)
    deck1 = gen_rand_deck("deck1", 0)

    # defining a 7 player uno game
    player1 = game_classes.Player("player_1")
    player1.grab_cards(deck1, 7)

    player2AI = game_AI.make_AI_basic(deck1, "player_2AI", 7)
    player3AI = game_AI.make_AI_basic(deck1, "player_3AI", 7)
    player4AI = game_AI.make_AI_basic(deck1, "player_4AI", 7)
    player5AI = game_AI.make_AI_basic(deck1, "player_5AI", 7)
    player6AI = game_AI.make_AI_basic(deck1, "player_6AI", 7)
    player7AI = game_AI.make_AI_basic(deck1, "player_7AI", 7)

    display.redraw_hand_visble(player1, None)

    # enters into playing the game
    game_logic.game_loop(board1, deck1, [player1, player2AI, player3AI, player4AI,
                                         player5AI, player6AI, player7AI])
