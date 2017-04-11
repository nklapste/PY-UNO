from AI_classes import Branch
from AI_classes import Leaf
import game_classes


def travel_Card_Guess_Tree(Card_Tree, max_depth):
    """
    Function that recursively travels Card_Guess_Tree.

    O(n) runtime which is bounded by max_depth
    """
    # list that will be appened card data in the format of
    # [(card1_color, depth), (card1_type, depth), (card2_color, depth)...]
    Card_Guess_list = []

    def travel_recus(Card_Tree, depth):
        """
        O(1) runtime
        """
        if Card_Tree is None:
            return
        (left_tree, right_tree) = read_Card_Tree_basic(Card_Tree)  # O(1)

        # case were no card is at this level of memory just return
        if left_tree is None and right_tree is None:
            return None
            pass
        # get this levels card data (color and type) and append to
        # Card_Guess_list
        (Card_color_p, Card_Type_p, Card_Played_By) = read_Card_Tree_values(
            right_tree, depth)  # O(1)
        Card_Guess_list.append(Card_color_p)  # O(1)
        Card_Guess_list.append(Card_Type_p)  # O(1)
        Card_Guess_list.append(Card_Played_By)  # O(1)

        # go to the next level of Card_Guess_Tree which is in the left_tree
        travel_recus(left_tree, depth + 3)

        return None

    travel_recus(Card_Tree, 0)
    slice_num = None
    # find the point in Card_Guess_list where the maximum depth is passed
    for i in range(len(Card_Guess_list)):  # O(n)
        (card_data, depth) = Card_Guess_list[i]

        if depth >= max_depth:
            slice_num = i
            break

    # if the maximum depth is passed slice the Card_Guess_list at this point
    if not (slice_num is None):
        Card_Guess_list = Card_Guess_list[:slice_num:]  # O(n)
    else:
        pass

    # list that will be appended pairs of the card_data (both the color and
    # type), note unlike Card_Guess_list depth data is removed.
    # The format is as follows (eg 3 max depth) [(card1_color, card1_type),
    # (card2_color, card2_type), (card3_color, None)]
    output_list = []

    # filter out the depth values for clean output and pair color and
    # type together
    for i in range(0, len(Card_Guess_list) - 2, 3):  # O(n)
        (card_data_1, depth_1) = Card_Guess_list[i]
        (card_data_2, depth_2) = Card_Guess_list[i + 1]
        (card_data_3, depth_3) = Card_Guess_list[i + 2]

        output_list.append((card_data_1, card_data_2, card_data_3))

    # if Card_Guess_list was odd above code would miss the last cards first
    # data value do to range iterating by 2
    if not len(Card_Guess_list) % 3 == 0:

        (card_data_1, depth_1) = Card_Guess_list[-2]
        (card_data_2, depth_2) = Card_Guess_list[-1]
        if card_data_1 is None:
            output_list.append((card_data_2, None, None))
        else:
            output_list.append((card_data_1, card_data_2, None))

    return output_list


def read_Card_Tree_values(Card_Tree, depth):
    """
    O(1) runtime
    """
    (Card_color, Card_Tree_2) = Card_Tree.get_offshoots()
    (Card_Type, played_by) = Card_Tree_2.get_offshoots()
    return ((Card_color.value, depth), (Card_Type.value, depth + 1), (played_by.value, depth + 2))


def read_Card_Tree_basic(Card_Tree):
    """
    O(1) runtime
    """
    (left_tree, right_tree) = Card_Tree.get_offshoots()
    return (left_tree, right_tree)


class Card_Guess_Tree:
    def __init__(self, name, max_depth=0):
        self.name = name
        self.Guess_Tree = None
        self.max_depth = max_depth

    # def gen_Card_Tree(self):
        start_Branch = Branch()
        self.Guess_Tree = start_Branch

    def read_card_tree(self):
        return travel_Card_Guess_Tree(self.Guess_Tree, self.max_depth)

    def update_card_tree(self, card):
        """
        O(1) runtime
        """
        Guess_Tree = self.Guess_Tree
        card_Branch_sub_1 = Branch(None, Leaf(card.type), Leaf(card.Owner))
        card_Branch = Branch(None, Leaf(card.color), card_Branch_sub_1)
        # add new card at new top of Card_Guess_Tree
        self.Guess_Tree = Branch(None, Guess_Tree, card_Branch)


def test_Card_Guess_Tree():
    """
    Function that tests all the base functions of implementing a
    Card_Guess_Tree: creating the treem adding new cards, and extracting
    cards with a memory limit.
    """
    test_tree = Card_Guess_Tree("test", 3)

    card1 = card_g = game_classes.Card("g_1", "small_cards/green_0.png", None)
    card2 = card_g = game_classes.Card("g_2", "small_cards/green_0.png", None)
    card3 = card_g = game_classes.Card("r_r", "small_cards/green_0.png", None)

    test_tree.update_card_tree(card3)
    test_tree.update_card_tree(card2)
    test_tree.update_card_tree(card1)
    test_tree.update_card_tree(card3)
    test_tree.update_card_tree(card2)
    test_tree.update_card_tree(card1)
    test_tree.update_card_tree(card3)
    test_tree.update_card_tree(card2)
    test_tree.update_card_tree(card1)
    test_tree.update_card_tree(card3)
    test_tree.update_card_tree(card2)
    test_tree.update_card_tree(card1)

    print(travel_Card_Guess_Tree(test_tree.Guess_Tree, 3))
    print(travel_Card_Guess_Tree(test_tree.Guess_Tree, 4))
    print(travel_Card_Guess_Tree(test_tree.Guess_Tree, 5))
    print(travel_Card_Guess_Tree(test_tree.Guess_Tree, 6))
    print(travel_Card_Guess_Tree(test_tree.Guess_Tree, 7))
