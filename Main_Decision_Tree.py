import AI_card_logic
from AI_classes import Branch
from AI_classes import Leaf
import AI_functs
import Card_Choose_Tree
import card_logic
from deck_gen import gen_rand_deck
import game_classes


def travel_Main_Decision_Tree(board, deck, player, players, Dec_Tree):
    """
    Function that recursively travels Main_Decision_Tree.

    O(n) runtime
    """

    (left_tree, right_tree) = read_Dec_tree(Dec_Tree)  #O(1)

    if left_tree is False:  # catch if Dec_Tree is actually a Leaf
        # print("Found Leaf:", right_tree)
        read_Dec_leaf_instruction(board, deck, player, players, right_tree)  # O(n)
        return
    else:
        question = Dec_Tree.question

        (left_yes, right_yes) = read_Dec_tree_question(
            board, player, players, question)  # O(n)

    # print("left or right:", left_yes, right_yes)
    if left_yes:
        travel_Main_Decision_Tree(board, deck, player, players, left_tree)  # O(n)
    elif right_yes:
        travel_Main_Decision_Tree(board, deck, player, players, right_tree)  # O(n)
    else:
        print("ERROR: didn't choose path")


def read_Dec_tree(Dec_Tree):
    """
    Main_Decision_Tree extraction function. Will try to extract a leaf
    value first, if this fails its expected that it is instead a branch.
    As such the branches offshoots are then extracted.

    O(1) runtime
    """
    try:
        Leaf_val = Dec_Tree.value
        return (False, Leaf_val)  # return special case

    except AttributeError:  # Dec_Tree is not a Leaf
        (left_tree, right_tree) = Dec_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Dec_tree_question(board, player, players, question):
    """
    Function that takes a branches question and returns a tuple of two Logic
    values. Indicating wether to go left or right within the tree.

    (True, False) ==> go left
    (False, True) ==> go right

    Any other combination is considered incorrect

    O(n) runtime where n is the length of players or the size of player's hand
    (whichever is larger)
    """
    # print("AI question:", player.name, question)

    if question == "Can I win this turn?":
        wild_count = 0
        for card in player.hand:  # O(n)
            if card.color == "w":
                wild_count += 1

        if wild_count >= len(player.hand) - 1:
            return (True, False)
        else:
            return (False, True)

    elif question == "Is there an apparent winner?":
        (winnners_bool, winners_list) = AI_functs.fetch_possible_winner(
            board, player, players)  # O(n)
        if winnners_bool:
            return (True, False)
        else:
            return (False, True)

    elif question == "Can stop them winning it?":
        (winnners_bool, winners_list) = AI_functs.fetch_possible_winner(
            board, player, players)  # O(n)
        playable_cards = card_logic.card_allowed(board, player)  # O(n)

        for hand_index in playable_cards:  # O(n)
            possible_card = player.hand[hand_index]

            if possible_card.type in ["p", "s", "d"]:  # O(3)
                return (True, False)

        return (False, True)

    elif question == "Does oldest card play priority beat my hate play priority?":
        (old_val, card_index) = AI_functs.fetch_oldest_card(board, player)  # O(n)
        (hate_val, hate_player) = AI_functs.fetch_hate_priority(
            player, players)  # O(n)
        if hate_val <= old_val:  # TODO
            return (True, False)
        else:
            return (False, True)

    elif question == "Do I have playable cards?":
        playable_cards = card_logic.card_allowed(board, player)  # O(n)
        if len(playable_cards) > 0:
            return (True, False)
        else:
            return (False, True)

    elif question == "Do I multiple playable cards?":
        playable_cards = card_logic.card_allowed(board, player)  # O(n)
        if len(playable_cards) > 1:
            return (True, False)
        else:
            return (False, True)

    elif question == "Do I have playable hate cards?":
        hate_cards = AI_functs.fetch_hate_cards(board, player)  # O(n)
        if len(hate_cards) > 0:
            return (True, False)
        else:
            return (False, True)


def read_Dec_leaf_instruction(board, deck, player, players, Leaf_val):
    """
    Function that takes the instructions given by a tree Leaf value and commits
    into doing its requested action. Some Leaf values require other imports
    such as AI_Functs, while others require computation of board/player status
    to proceed.

    In some cases the tree Leaf value will result moving from using
    Main_Decision_Tree into computing a preffered playable card. As such
    Card_Choose_Tree is then accessed and traveled.

    O(n) runtime

    or

    Recuse Main_Decision_Tree or Card_Choose_Tree
    """
    # print("AI instruction:", player.name, Leaf_val)

    if Leaf_val == "Goto stop funct":  # TODO get runtime
        (winners_bool, possible_winners) = AI_functs.fetch_possible_winner(
            board, player, players)  # O(n)
        AI_functs.stop_winners(board, deck, player,
                               players, possible_winners[0])  # O(n)

    elif Leaf_val == "Play oldest playable card":
        (old_val, card_index) = AI_functs.fetch_oldest_card(board, player)  # O(n)
        player.play_card(board, card_index)

    elif Leaf_val == "Play highest hate playable card":
        (hate_val, hate_player) = AI_functs.fetch_hate_priority(
            player, players)  # O(n)
        hate_cards = AI_functs.fetch_hate_cards(board, player)  # O(n)
        player.play_card(board, hate_cards[0][1])
        # O(n) or recuse Main_Decision_Tree
        AI_card_logic.AI_card_played_type(
            board, deck, player, players, hate_player)

    elif Leaf_val == "Go back up this tree":
        # goes all back to the start of start_Branch_2 and goes right
        # this is needed to prevent an infinite recusion
        (branch_left_2, branch_right_1) = player.Main_Decision_Tree.Dec_Tree.get_offshoots()
        (branch_left_2, branch_right_2) = branch_right_1.get_offshoots()
        # recurse Main_Decision_Tree
        travel_Main_Decision_Tree(board, deck, player, players, branch_right_2)

    elif Leaf_val == "Do nothing":
        AI_functs.do_nothing(deck, player)  # O(1)

    elif Leaf_val == "Goto Card_Choose_Tree":
        # recurse Card_Choose_Tree
        Card_Choose_Tree.travel_Card_Choose_Tree(
            board, deck, player, players, player.Card_Choose_Tree.Choose_Tree)

    elif Leaf_val == "Goto play_win":
        AI_functs.play_win(board, deck, player, players)  # O(n)


class Main_Decision_Tree:
    def __init__(self, name, difficulty_level=0):
        self.name = name
        self.difficulty_level = difficulty_level
        self.Dec_Tree = None

        subBranch_1 = Branch("Can stop them winning it?", Leaf(
            "Goto stop funct"), Leaf("Go back up this tree"))

        subsubsubsubBranch_2_1 = Branch("Does oldest card play priority beat my hate play priority?", Leaf(
            "Goto Card_Choose_Tree"), Leaf("Play highest hate playable card"))

        subsubsubBranch_2_1 = Branch(
            "Do I have playable hate cards?", subsubsubsubBranch_2_1, Leaf("Goto Card_Choose_Tree"))

        subsubBranch_2_1 = Branch(
            "Do I multiple playable cards?", subsubsubBranch_2_1, Leaf("Goto Card_Choose_Tree"))

        subBranch_2 = Branch("Do I have playable cards?",
                             subsubBranch_2_1, Leaf("Do nothing"))

        start_Branch_2 = Branch(
            "Is there an apparent winner?", subBranch_1, subBranch_2)

        start_Branch_1 = Branch("Can I win this turn?", Leaf(
            "Goto play_win"), start_Branch_2)

        self.Dec_Tree = start_Branch_1


def test_Main_Decision_Tree_2():
    """
    Test function that tests the basic capabilites of a Main_Decision_Tree
    going over feature such as creating a Main_Decision_Tree, and deciding a
    player decision based on board state.
    """

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
