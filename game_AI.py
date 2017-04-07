import Card_Choose_Tree
import Card_Guess_Tree
import game_classes
import Main_Decision_Tree


def make_AI_basic(deck, AI_name, mem_depth=0, difficulty_level=0):
    AI_player_gen = game_classes.Player(AI_name)
    # grab an initial hand
    AI_player_gen.grab_cards(deck, 7)

    AI_player_gen.Main_Decision_Tree = Main_Decision_Tree(AI_name)
    AI_player_gen.Card_Guess_Tree = Card_Guess_Tree(AI_name, mem_depth)
    AI_player_gen.Card_Choose_Tree = Card_Choose_Tree(AI_name)

    return AI_player_gen


# TODO
def make_AI(AI_name, difficulty_level=0, difficulty_level_list=None):
    """
    Function that handels all the initilizing of tree structures needed for
    an PY-UNO AI needs to be created. Additional features (difficulty addons)
    can be selected by either a simple difficulty level number (0-10) 0 = dumb
    10 = card counting god. Manual difficulty features can be individually
    enabled by a optional input logical list.

    Returns: an Player class from game_classes.py that is AI controlled via a
    decision tree method.
    """

    AI_gen = game_classes.Player(AI_name)
    AI_gen.AI = True

    if difficulty_level == 0:

        pass

    elif difficulty_level == 1:

        pass

    elif difficulty_level == 2:

        pass

    elif difficulty_level == 3:

        pass

    elif difficulty_level == 4:
        pass

    elif difficulty_level == 5:

        pass

    elif difficulty_level == 6:

        pass

    elif difficulty_level == 7:

        pass

    elif difficulty_level == 8:

        pass

    elif difficulty_level == 9:

        pass

    elif difficulty_level == 10:

        pass

    return AI_gen
