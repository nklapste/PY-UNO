import AI_card_logic
from AI_classes import Branch
from AI_classes import Leaf
import AI_functs
import card_logic
from deck_gen import gen_rand_deck
import game_classes


def travel_Card_Choose_Tree(board, deck, player, players, Card_Choose_Tree):
    """
    Function that recursively travels Card_Choose_Tree.

    O(n) runtime
    """
    (left_tree, right_tree) = read_Card_Choose_Tree(Card_Choose_Tree)  # O(1)

    if left_tree is False:  # catchi if Card_Choose_Tree is actually a Leaf
        # print("Found Leaf:", right_tree)
        read_Card_Choose_Leaf_instruction(
            board, deck, player, players, right_tree)  # O(n)
        return
    else:
        question = Card_Choose_Tree.question

        (left_yes, right_yes) = read_Card_Choose_Tree_question(
            board, player, players, question)  # O(n)

    # print("left or right:", left_yes, right_yes)
    if left_yes:
        travel_Card_Choose_Tree(board, deck, player,
                                players, left_tree)  # O(n)
    elif right_yes:
        travel_Card_Choose_Tree(board, deck, player,
                                players, right_tree)  # O(n)
    else:
        print("ERROR: didn't choose path")


def read_Card_Choose_Tree(Card_Choose_Tree):
    """
    Card_Choose_Tree extraction function. Will try to extract a leaf value
    first, if this fails its expected that it is instead a branch. As such
    the branches offshoots are then extracted.

    O(1) runtime
    """
    try:  # check if Card_Choose_Tree is actually is
        Leaf_val = Card_Choose_Tree.value
        return (False, Leaf_val)  # return special case

    except AttributeError:  # Card_Choose_Tree is not a Leaf
        (left_tree, right_tree) = Card_Choose_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Card_Choose_Tree_question(board, player, players, question):
    """
    Function that takes a branches question and returns a tuple of two Logic
    values. Indicating wether to go left or right within the tree.

    (True, False) ==> go left
    (False, True) ==> go right

    Any other combination is considered incorrect

    O(n) runtime where n is the number of cards in a players hand
    """
    # print("AI question:", player.name, question)

    if question == "Do I multiple playable cards?":

        if len(player.hand) > 1:
            return (True, False)
        else:
            return (False, True)

    elif question == "Do I have a nonwild playable card?":

        allowed_cards = card_logic.card_allowed(board, player)  # O(n)
        for i in allowed_cards:  # O(n)
            if not player.hand[i].color == "w":
                return (True, False)

        return (False, True)

    elif question == "what is my most common (color or type) that is also playable?":

        max_color = AI_functs.fetch_most_common_color_playable(
            board, player)  # O(n)
        max_type = AI_functs.fetch_most_common_type_playable(
            board, player)    # O(n)

        max_color_count = 0
        max_type_count = 0
        for card in player.hand:  # O(n)
            if card.color == max_color:
                max_color_count += 1
            if card.type == max_type:
                max_type_count += 1

        if max_color_count >= max_type_count:
            return (True, False)
        else:
            return (False, True)


def read_Card_Choose_Leaf_instruction(board, deck, player, players, Leaf_val):
    """
    Function that takes the instructions given by a tree Leaf value and commits
    into doing its requested action. Some Leaf values require other imports
    such as AI_Functs, while others require computation of board/player status
    to proceed.

    O(n) runtime where n is the lenght of players or the size of player's hand
    (whichever is bigger)

    or

    Can recuse back to Main_Decision_Tree
    """
    # print("AI instruction:", player.name, Leaf_val)

    if Leaf_val == "Play only card":

        allowed_cards = card_logic.card_allowed(board, player)  # O(n)
        player.play_card(board, allowed_cards[0])

    elif Leaf_val == "play wild, most common color":
        # search for wild card messy method
        hand_index = 0
        for card in player.hand:  # O(n)
            if card.color == "w":
                player.play_card(board, hand_index)
                break
            hand_index += 1

    elif Leaf_val == "play most common color":

        color_max = AI_functs.fetch_most_common_color_playable(
            board, player)  # O(n)

        allowed_cards = card_logic.card_allowed(board, player)  # O(n)

        for i in allowed_cards:  # O(n)
            if player.hand[i].color == color_max:
                player.play_card(board, i)
                break

    elif Leaf_val == "play most common type":

        type_max = AI_functs.fetch_most_common_type_playable(
            board, player)  # O(n)

        allowed_cards = card_logic.card_allowed(board, player)  # O(n)

        for i in allowed_cards:  # O(n)
            if player.hand[i].type == type_max:
                player.play_card(board, i)

                break

    # figure out what do within the game from AI played card
    AI_card_logic.AI_card_played_type(board, deck, player, players)  # O(n)


class Card_Choose_Tree:
    def __init__(self, name):
        self.name = name

        subBranch_1 = Branch(
            "what is my most common (color or type) that is also playable?",
            Leaf("play most common color"), Leaf("play most common type"))

        Branch_1 = Branch("Do I have a nonwild playable card?",
                          subBranch_1, Leaf("play wild, most common color"))

        start_Branch = Branch(
            "Do I multiple playable cards?", Branch_1, Leaf("Play only card"))

        self.Choose_Tree = start_Branch


def test_Card_Choose_Tree():
    """
    Test function that tests the basic capabilites of a Card_Choose_Tree
    going over feature such as creating a Card_Choose_Tree, and deciding a
    card decision based on board state (thus traveling the tree itself).
    """
    test_tree = Card_Choose_Tree("test")

    test_board = game_classes.Board("board_test")
    deck1 = gen_rand_deck("deck_test", 0)

    player1 = game_classes.Player("player_1")
    player1.grab_cards(deck1, 7)

    player2AI = game_classes.Player("player_2AI")
    player2AI.grab_cards(deck1, 7)

    player3AI = game_classes.Player("player_3AI")
    player3AI.grab_cards(deck1, 7)

    player4AI = game_classes.Player("player_4AI")
    player4AI.grab_cards(deck1, 7)

    player5AI = game_classes.Player("player_5AI")
    player5AI.grab_cards(deck1, 7)

    player6AI = game_classes.Player("player_6AI")
    player6AI.grab_cards(deck1, 7)

    player7AI = game_classes.Player("player_7AI")
    player7AI.grab_cards(deck1, 7)

    test_player = player1
    test_players = [player1, player2AI, player3AI, player4AI,
                    player5AI, player6AI, player7AI]

    travel_Card_Choose_Tree(test_board, test_player,
                            test_players, test_tree.Choose_Tree)
