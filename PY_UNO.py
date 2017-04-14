from deck_gen import gen_rand_deck
import display_funct
import game_AI
import game_classes
import game_logic

# loop for allowing multiple games to be restarted
while True:
    # initilizing the board to be used within the game
    board1 = game_classes.Board("board1")

    # initilizing a deck to be used within the game (3 copies are added to
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

    display_funct.redraw_hand_visble(player1, None)


    # enters into playing the game
    game_logic.game_loop(board1, deck1, [player1, player2AI, player3AI, player4AI,
                         player5AI, player6AI, player7AI])
