

def travel_Main_Decision_Tree(Dec_Tree):
    '''
    TODO: SHOULD READ QUESTIUON THEN PROCEED LEFT OR RIGHT
    '''
    (left_tree, right_tree) = read_Dec_tree(Dec_Tree)

    if left_tree is False:  # catchi if Dec_Tree is actually a Leaf
        # TODO do leaf instruction
        read_Dec_leaf_instruction(right_tree)
        pass
    else:
        question = Dec_Tree.question

        (left_yes, right_yes) = read_Dec_tree_question(question):

    if left_yes:
        travel_Main_Decision_Tree(left_tree)
    elif right_yes:
        travel_Main_Decision_Tree(right_tree)
    else:
        print("ERROR: didn't choose path")


def read_Dec_tree(Dec_Tree):

    try:  # check if Dec_Tree is actually is
        leaf_val = Dec_Tree.value
        return (False, leaf_val)  # return special case

    except TypeError:  # Dec_Tree is not a Leaf
        (left_tree, right_tree) = Dec_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Dec_tree_question(question):
    left_yes = False
    right_yes = False
    if question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    return (left_yes, right_yes)


def read_Dec_leaf_instruction(leaf_val):
    if leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

#########################################################


def fetch_oldest_card():
    pass


def check_possible_winner(Board, players):
    pass


def play_card(Board, player):
    pass


def fetch_hate_priority():
    pass


def do_nothing():
    pass

#########################################################
