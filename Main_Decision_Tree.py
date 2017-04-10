import AI_functs
import game_classes
from AI_classes import Branch
from AI_classes import Leaf
from deck_gen import gen_rand_deck
import card_logic
import Card_Choose_Tree
import AI_card_logic


def travel_Main_Decision_Tree(board, deck, player, players, Dec_Tree):
    """
    Function that recursively travels Main_Decision_Tree.
    """

    (left_tree, right_tree) = read_Dec_tree(Dec_Tree)

    if left_tree is False:  # catch if Dec_Tree is actually a Leaf
        print("Found Leaf:", right_tree)
        read_Dec_leaf_instruction(board, deck, player, players, right_tree)
        return
    else:
        question = Dec_Tree.question

        (left_yes, right_yes) = read_Dec_tree_question(
            board, player, players, question)

    print("left or right:", left_yes, right_yes)
    if left_yes:
        travel_Main_Decision_Tree(board, deck, player, players, left_tree)
    elif right_yes:
        travel_Main_Decision_Tree(board, deck, player, players, right_tree)
    else:
        print("ERROR: didn't choose path")


def read_Dec_tree(Dec_Tree):
    try:
        Leaf_val = Dec_Tree.value
        return (False, Leaf_val)  # return special case

    except AttributeError:  # Dec_Tree is not a Leaf
        (left_tree, right_tree) = Dec_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Dec_tree_question(board, player, players, question):
    left_yes = False
    right_yes = False
    print("AI question:", player.name, question)

    if question == "Is there an apparent winner?":
        (winnners_bool, winners_list) = AI_functs.fetch_possible_winner(
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

            if possible_card.type in ["p", "s", "d"]:
                return (True, False)

        return (False, True)

    elif question == "Does oldest card play priority beat my hate play priority?":
        (old_val, card_index) = AI_functs.fetch_oldest_card(board, player)
        (hate_val, hate_player) = AI_functs.fetch_hate_priority(player, players)
        print((old_val, card_index), (hate_val, hate_player))
        if hate_val <= old_val:  # TODO
            return (True, False)
        else:
            return (False, True)

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

    elif question == "Do I have playable hate cards?":
        hate_cards = AI_functs.fetch_hate_cards(board, player)
        if len(hate_cards) > 0:
            return (True, False)
        else:
            return (False, True)

    elif question == "1":
        pass

    return (left_yes, right_yes)


def read_Dec_leaf_instruction(board, deck, player, players, Leaf_val):

    print("AI instruction:", player.name, Leaf_val)

    if Leaf_val == "Goto stop funct": #TODO
        (winners_bool, possible_winners) = AI_functs.fetch_possible_winner(board, player, players)
        AI_functs.stop_winners(board, deck, player, possible_winners[0])

    elif Leaf_val == "Play oldest playable card":  # TODO obsolete
        (old_val, card_index) = AI_functs.fetch_oldest_card(board, player)
        player.play_card(board, card_index)

    elif Leaf_val == "Play highest hate playable card":  # TODO
        (hate_val, hate_player) = AI_functs.fetch_hate_priority(player, players)
        hate_cards = fetch_hate_cards(player)
        player.play_card(board, hate_cards[0][1])
        AI_card_logic.AI_card_played_type(board, deck, player, players, hate_player)

    elif Leaf_val == "Play a card":
        Card_Choose_Tree.travel_Card_Choose_Tree(
            board, deck, player, players, player.Card_Choose_Tree.Choose_Tree)

    elif Leaf_val == "Go back up this tree":  # goes all back to the start and goes right

        (branch_left, branch_right) = player.Main_Decision_Tree.Dec_Tree.get_offshoots()
        travel_Main_Decision_Tree(board, deck, player, players, branch_right)

    elif Leaf_val == "Do nothing":
        AI_functs.do_nothing(deck, player)
        pass
        
    elif Leaf_val == "Goto Card_Choose_Tree":
        Card_Choose_Tree.travel_Card_Choose_Tree(
            board, deck, player, players, player.Card_Choose_Tree.Choose_Tree)


class Main_Decision_Tree:
    def __init__(self, name, difficulty_level=0):
        self.name = name
        self.difficulty_level = difficulty_level
        self.Dec_Tree = None

        subBranch_1 = Branch("Can stop them winning it?", Leaf(
            "Goto stop funct"), Leaf("Go back up this tree"))

        subsubsubsubBranch_2_1 = Branch("Does oldest card play priority beat my hate play priority?", Leaf(
            "Goto Card_Choose_Tree"), Leaf("Play highest hate playable card"))  # TODO

        subsubsubBranch_2_1 = Branch(
            "Do I have playable hate cards?", subsubsubsubBranch_2_1, Leaf("Goto Card_Choose_Tree"))

        subsubBranch_2_1 = Branch(
            "Do I multiple playable cards?", subsubsubBranch_2_1, Leaf("Play a card"))

        subBranch_2 = Branch("Do I have playable cards?",
                             subsubBranch_2_1, Leaf("Do nothing"))

        start_Branch = Branch(
            "Is there an apparent winner?", subBranch_1, subBranch_2)

        self.Dec_Tree = start_Branch


def test_Main_Decision_Tree_1():
    test = Main_Decision_Tree("test", 2)
    test.gen_Dec_Tree()
    level_0 = test.Dec_Tree
    (level_1_L, level_1_R) = test.Dec_Tree.get_offshoots()
    (level_2_1_L_L, level_2_1_L_R) = level_1_L.get_offshoots()
    print(level_2_1_L_L.value)
    print(level_2_1_L_R.value)


def test_Main_Decision_Tree_2():

    test_tree = Main_Decision_Tree("test")

    test_board = game_classes.Board("board_test")
    deck1 = gen_rand_deck("deck_test", 0)

    player1 = game_classes.Player("player_1")
    player1.grab_cards(deck1, 8)

    player2AI = game_classes.Player("player_2AI")
    player2AI.grab_cards(deck1, 1)

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

    player1.Main_Decision_Tree = test_tree
    player1.Card_Choose_Tree = Card_Choose_Tree.Card_Choose_Tree("test")

    for i in range(len(player1.hand)):
        print(player1.hand[i].name)
        player1.hand[i].old_val = i

    test_player = player1

    test_players = [player1, player2AI, player3AI, player4AI,
                    player5AI, player6AI, player7AI]

    travel_Main_Decision_Tree(test_board, deck1, test_player,
                              test_players, test_tree.Dec_Tree)
    print(test_board.card_stack[-1].name)


test_Main_Decision_Tree_2()
