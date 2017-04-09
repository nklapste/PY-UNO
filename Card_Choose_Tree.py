import card_logic
import game_classes
from AI_classes import Leaf
from AI_classes import Branch


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

    if left_yes:
        travel_Card_Choose_Tree(board, player, players, left_tree)
    elif right_yes:
        travel_Card_Choose_Tree(board, player, players, right_tree)
    else:
        print("ERROR: didn't choose path")


def read_Card_Choose_Tree(Card_Choose_Tree):

    try:  # check if Card_Choose_Tree is actually is
        Leaf_val = Card_Choose_Tree.value
        return (False, Leaf_val)  # return special case

    except TypeError:  # Card_Choose_Tree is not a Leaf
        (left_tree, right_tree) = Card_Choose_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Card_Choose_Tree_question(board, player, players, question):
    # TODO
    left_yes = False
    right_yes = False

    if question == "Do I multiple playable cards?":
        if len(player.hand) > 1:
            return (True, False)

    elif question == "Do I have a nonwild playable card?":
        allowed_cards = card_logic.card_allowed(board, player)
        for i in allowed_cards:
            if not player.hand[i].color == "w":
                return (True, False)
        return (False, True)

    elif question == "what is my most common (color or type) that is also playable?":
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

    return (left_yes, right_yes)


def read_Card_Choose_Leaf_instruction(board, player, players, Leaf_val):
    # TODO INCLUDE BOARD AND PLAYER
    if Leaf_val == "Play only card":
        allowed_cards = card_logic.card_allowed(board, player)
        AI_functs.play_card(board, player, allowed_cards[0])

    elif Leaf_val == "play wild, most common color":  # TODO
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
        allowed_cards = card_logic.card_allowed(board, player)
        for i in allowed_cards:  # TODO
            player.hand[i].color

        common_color = AI_functs.fetch_most_common_color(
            player, read_Card_Choose_Tree)
        for i in allowed_cards:
            if player.hand[i].color == common_color:
                AI_functs.play_card(board, player, i)
                break

    elif Leaf_val == "play most common type":  # TODO
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
