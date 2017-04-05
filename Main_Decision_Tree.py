import game_classes
import AI_functs
import Leaf from AI_classes
import Branch from AI_classes

def travel_Main_Decision_Tree(Dec_Tree):
    '''
    TODO: SHOULD READ QUESTIUON THEN PROCEED LEFT OR RIGHT
    '''
    (left_tree, right_tree) = read_Dec_tree(Dec_Tree)

    if left_tree is False:  # catchi if Dec_Tree is actually a Leaf
        # TODO do leaf instruction
        read_Dec_leaf_instruction(right_tree)
        return
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

    try:  # check
 if Dec_Tree is actually is
        leaf_val = Dec_Tree.value
        return (False, leaf_val)  # return special case

    except TypeError:  # Dec_Tree is not a Leaf
        (left_tree, right_tree) = Dec_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Dec_tree_question(question):
    left_yes = False
    right_yes = False

    if question == "Is there an apparent winner?":
        (winnners_bool, winners_list) =  AI_functs.fetch_possible_winner(
            board, player, players)
        if winnners_bool:
            return (True, False)
        else:
            return (False, True)

    elif question == "Can stop them winning it?":
        (winnners_bool, winners_list) = AI_functs.fetch_possible_winner(
            board, player, players)
        playable_cards = card_logic.card_allowed(board, player)

        for hand_index in playable_cards:
            possible_card = player.hand[hand_index]

            if card.type in ["p", "s", "r", "d"]:
                return (True, False)

        return (False, True)

    elif question == "Does oldest card play priority beat my hate play priority?":
        old_val = fetch_oldest_card(player)
        (hate_val, hate_player) = AI_functs.fetch_hate_priority(players)
        if hate_val < oldval:
            return (True, False)
        else:
            return (True, False)

    elif question == "Do I have playable cards?":
        playable_cards = card_logic.card_allowed(board, player)
        if len(playable_cards) > 0:
            return (True, False)
        else:
            return (False, True)

    elif question == "Do I multiple playable cards?":
        playable_cards = card_logic.card_allowed(board, player)
            if len(playable_cards) > 1:
                return (True, False)
            else:
                return (False, True)

    elif question == "1":
        pass

    elif question == "1":
        pass

    return (left_yes, right_yes)


def read_Dec_leaf_instruction(leaf_val):
    # TODO INCLUDE BOARD AND PLAYER
    if leaf_val == "Goto stop funct":
        stop_winners(board, player, possible_winners)
        pass

    elif leaf_val == "Play old card":
        pass

    elif leaf_val == "Play hate card":
        pass

    elif leaf_val == "Play a card":
        playable_cards = card_logic.card_allowed(board, player)
        player.play_card(board, playable_cards[0])
        pass

    elif leaf_val == "Go back up this tree":  # goes all back to the start and goes right
        (branch_left, branch_right) = player.Main_Dec.Dec_Tree.get_offshoots()
        travel_Main_Decision_Tree(branch_right)

    elif leaf_val == "1":
        pass

    elif leaf_val == "Do nothing":
        do_nothing()
        pass



class Main_Decision_Tree:
    def __init__(self, name, difficulty_level=0):
        self.name = name
        self.difficulty_level = difficulty_level
        self.Dec_Tree = None

    def gen_Dec_Tree(self):
        # TODO
        subBranch_1 = Branch("Can stop them winning it?", Leaf(
            "Goto stop funct"), Leaf("Go back up this tree"))

        subsubsubBranch_2_1 = Branch("Does oldest card play priority beat my hate play priority?", Leaf(
            "Play old card"), Leaf("Play hate card"))  # TODO

        subsubBranch_2_1 = Branch(
            "Do I multiple playable cards?", subsubsubBranch_2_1, Leaf("Play a card"))

        subBranch_2 = Branch("Do I have playable cards?",
                             subsubBranch_2_1, Leaf("Do nothing"))

        start_Branch = Branch(
            "Is there an apparent winner?", subBranch_1, subBranch_2)

        self.Dec_Tree = start_Branch


def test_Main_Decision_Tree():
    test = Main_Decision_Tree("test", 2)
    test.gen_Dec_Tree()
    level_0 = test.Dec_Tree
    (level_1_L, level_1_R) = test.Dec_Tree.get_offshoots()
    (level_2_1_L_L, level_2_1_L_R) = level_1_L.get_offshoots()
    print(level_2_1_L_L.value)
    print(level_2_1_L_R.value)
