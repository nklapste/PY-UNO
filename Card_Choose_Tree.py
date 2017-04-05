import game_classes
import Leaf from AI_classes
import Branch from AI_classes


def travel_Card_Choose_Tree(Card_Choose_Tree):
    '''
    TODO: SHOULD READ QUESTIUON THEN PROCEED LEFT OR RIGHT
    '''
    (left_tree, right_tree) = read_Card_Choose_Tree(Card_Choose_Tree)

    if left_tree is False:  # catchi if Card_Choose_Tree is actually a Leaf
        # TODO do Leaf instruction
        read_Card_Choose_Leaf_instruction(right_tree)
        return
    else:
        question = Card_Choose_Tree.question

        (left_yes, right_yes) = read_Card_Choose_Tree_question(question):

    if left_yes:
        travel_Card_Choose_Tree(left_tree)
    elif right_yes:
        travel_Card_Choose_Tree(right_tree)
    else:
        print("ERROR: didn't choose path")


def read_Card_Choose_Tree(Card_Choose_Tree):

    try:  # check if Card_Choose_Tree is actually is
        Leaf_val = Card_Choose_Tree.value
        return (False, Leaf_val)  # return special case

    except TypeError:  # Card_Choose_Tree is not a Leaf
        (left_tree, right_tree) = Card_Choose_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Card_Choose_Tree_question(question):
    # TODO
    left_yes = False
    right_yes = False

    if question == "Do I multiple playable cards?":
        pass
    elif question == "Do I have a nonwild playable card?":
        pass
    elif question == "what is my most common (color or type) that is also playable?":
        pass

    return (left_yes, right_yes)


def read_Card_Choose_Leaf_instruction(Leaf_val):
    # TODO INCLUDE BOARD AND PLAYER
    if Leaf_val == "Play only card":
        pass
    elif Leaf_val == "play wild, most common color":
        pass
    elif Leaf_val == "play most common color":
        pass
    elif Leaf_val == "play most common type":
        pass


class Card_Choose_Tree:
    def __init__(self, name, max_depth=0):
        self.name = name
        self.Card_Choose_Tree = None

    def gen_Card_Chooes_Tree(self):

        subBranch_1 = Branch(
            "what is my most common (color or type) that is also playable?",
            Leaf("play most common color"), Leaf("play most common type"))

        Branch_1 = Branch("Do I have a nonwild playable card?",
                          subBranch_1, Leaf("play wild, most common color"))

        start_Branch = Branch(
            "Do I multiple playable cards?", Branch_1, Leaf("Play only card"))

        self.Card_Choose_Tree = start_Branch
