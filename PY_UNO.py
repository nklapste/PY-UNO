from deck_gen import gen_rand_deck
import game_classes
import game_logic
import pygame
import display_funct

pygame.init()

# default rectangle size
def_rect = pygame.Rect(0, 0, 130, 182)
face_down_card = game_classes.Card(
    "face_down", "small_cards/card_back.png", None)

# initilizing the board to be used within the game
board1 = game_classes.Board("board1")
# initilizing a deck to be used within the game (3 copies are added to each other)
deck1 = gen_rand_deck("deck1", 3)

# defining a 3 player uno game
player1 = game_classes.Player("player_1")
player1.grab_cards(deck1, 7)

player2AI = game_classes.Player("player_2AI")
player2AI.grab_cards(deck1, 7)

player3AI = game_classes.Player("player_3AI")
player3AI.grab_cards(deck1, 7)

display_funct.redraw_hand_visble(player1, None)

card = player1.hand[0]
card.rect = card.rect.move(0, -100)

########################################################

# loop function that enteres into playing the game
game_logic.game_loop(board1, deck1, [player1, player2AI, player3AI])

########################################################
