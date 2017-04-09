import card_logic
import game_classes
from AI_classes import Leaf
from AI_classes import Branch
from deck_gen import gen_rand_deck
import AI_functs

def travel_Card_Choose_Tree(board, player, players, Card_Choose_Tree):
    """
    Function that recursively travels Card_Choose_Tree.
    """

    (left_tree, right_tree) = read_Card_Choose_Tree(Card_Choose_Tree)

    if left_tree is False:  # catchi if Card_Choose_Tree is actually a Leaf
        # TODO do Leaf instruction
        read_Card_Choose_Leaf_instruction(board, player, players, right_tree)
        return
    else:
        question = Card_Choose_Tree.question

        (left_yes, right_yes) = read_Card_Choose_Tree_question(
            board, player, players, question)

    print(left_yes, right_yes)
    if left_yes:
        travel_Card_Choose_Tree(board, player, players, left_tree)
    elif right_yes:
        travel_Card_Choose_Tree(board, player, players, right_tree)
    else:
        print("ERROR: didn't choose path")


def read_Card_Choose_Tree(Card_Choose_Tree):
    # TODO print(Card_Choose_Tree)
    try:  # check if Card_Choose_Tree is actually is
        Leaf_val = Card_Choose_Tree.value
        return (False, Leaf_val)  # return special case

    except AttributeError:  # Card_Choose_Tree is not a Leaf
        (left_tree, right_tree) = Card_Choose_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Card_Choose_Tree_question(board, player, players, question):
    # TODO
    left_yes = False
    right_yes = False

    if question == "Do I multiple playable cards?":
        print("AI question:", player.name, question)

        if len(player.hand) > 1:
            return (True, False)
        else:
            return (False, True)

    elif question == "Do I have a nonwild playable card?":
        print("AI question:", player.name, question)

        allowed_cards = card_logic.card_allowed(board, player)
        for i in allowed_cards:
            if not player.hand[i].color == "w":
                return (True, False)
        return (False, True)

    elif question == "what is my most common (color or type) that is also playable?":
        print("AI question:", player.name, question)

        # TODO NEED RETHINKING
        type_dict = dict()
        color_dict = dict()

        allowed_cards = card_logic.card_allowed(board, player)
        for i in allowed_cards:
            allowed_card = player.hand[i]

            try:
                color_dict[allowed_card.color] = color_dict[allowed_card.color] + 1
            except KeyError:
                color_dict[allowed_card.color] = 1

            try:
                type_dict[allowed_card.type] = type_dict[allowed_card.type] + 1
            except KeyError:
                type_dict[allowed_card.type] = 1
        #TODO
        print(type_dict, color_dict)
        print(max(type_dict, key=type_dict.get))
        print(max(color_dict, key=color_dict.get))

        if color_dict[max(color_dict, key=color_dict.get)] > type_dict[max(type_dict, key=type_dict.get)]:
            return (True, False)
        else:
            return (False, True)

    return (left_yes, right_yes)


def read_Card_Choose_Leaf_instruction(board, player, players, Leaf_val):
    # TODO INCLUDE BOARD AND PLAYER
    if Leaf_val == "Play only card":
        print("AI instruction:", player.name, Leaf_val)

        allowed_cards = card_logic.card_allowed(board, player)
        AI_functs.play_card(board, player, allowed_cards[0])

    elif Leaf_val == "play wild, most common color":  # TODO
        print("AI instruction:", player.name, Leaf_val)

        common_color = AI_functs.fetch_most_common_color(player)

        # search for wild card messy method
        hand_index = 0
        for card in player.hand:
            if card.color == "w":
                AI_functs.play_card(board, player, hand_index)

                if card.type == "p":  # TODO SPECIAL CASE FOR DRAW FOUR

                    break
            hand_index += 1

        # set the board to the common_color
        board.color = common_color
        # read card choose tree again to play a another card
        read_Card_Choose_Tree(Card_Choose_Tree)

        # TODO play wild card aI

    elif Leaf_val == "play most common color":  # TODO
        print("AI instruction:", player.name, Leaf_val)

        allowed_cards = card_logic.card_allowed(board, player)
        for i in allowed_cards:  # TODO
            player.hand[i].color

        common_color = AI_functs.fetch_most_common_color(
            player)
        for i in allowed_cards:
            if player.hand[i].color == common_color:
                AI_functs.play_card(board, player, i)
                break

    elif Leaf_val == "play most common type":  # TODO
        print("AI instruction:", player.name, Leaf_val)

        allowed_cards = card_logic.card_allowed(board, player)
        common_type = AI_functs.fetch_most_common_type(player)
        for i in allowed_cards:
            if player.hand[i].type == common_type:
                AI_functs.play_card(board, player, i)
                break


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


    travel_Card_Choose_Tree(test_board, test_player, test_players, test_tree.Choose_Tree)



test_Card_Choose_Tree()
