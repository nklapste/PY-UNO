from deck_gen import gen_rand_deck
import display_funct
import game_classes
import game_logic
import pygame
import game_AI


pygame.init()

# default rectangle size
def_rect = pygame.Rect(0, 0, 130, 182)
face_down_card = game_classes.Card(
    "face_down", "small_cards/card_back.png", None)

# initilizing the board to be used within the game
board1 = game_classes.Board("board1")

# initilizing a deck to be used within the game (3 copies are added to
# each other)
deck1 = gen_rand_deck("deck1", 0)

# defining a 2 player uno game
player1 = game_classes.Player("player_1")
player1.grab_cards(deck1, 7)

# player2AI = game_classes.Player("player_2AI")
# player2AI.grab_cards(deck1, 7)

player2AI = game_AI.make_AI_basic(deck1, "player_2AI", 5, difficulty_level=0)

display_funct.redraw_hand_visble(player1, None)

########################################################

# loop function that enteres into playing the game
game_logic.game_loop(board1, deck1, [player1, player2AI])

########################################################
