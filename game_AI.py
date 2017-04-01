import AI_classes
import game_classes


def make_AI(AI_name, difficulty_level=0, difficulty_level_list=None):
    '''
    Function that handels all the initilizing of tree structures needed for
    an PY-UNO AI needs to be created. Additional features (difficulty addons)
    can be selected by either a simple difficulty level number (0-10) 0 = dumb
    10 = card counting god. Manual difficulty features can be individually
    enabled by a optional input logical list.

    Returns: an Player class from game_classes.py that is AI controlled via a
    decision tree method.
    '''
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





def main_decision_tree():
    '''
    '''

    def initilize_tree():
        Tree_gen = AI_classes.branch(AI_classes.branch, AI_classes.Leaf("fag"))
        Tree_gen.child1.child1 = [1]

        return Tree_gen
    return initilize_tree()
print(main_decision_tree())
print(main_decision_tree().child1)
print(main_decision_tree().child2)
print(main_decision_tree().child1.child1)
