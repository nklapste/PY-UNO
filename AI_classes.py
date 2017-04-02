

class Leaf:
    def __init__(self, value):
        self.value = value


class Branch:
    def __init__(self, Branch_q=None, child_1=None, child_2=None):
        self.child_1 = child_1
        self.child_2 = child_2
        self.question = Branch_q

    def get_offshoots(self):
        return (self.child_1, self.child_2)


class Main_Decision_Tree:
    def __init__(self, name, difficulty_level=0):
        self.name = name
        self.difficulty_level = difficulty_level
        self.Dec_Tree = None

    def gen_Dec_Tree(self):

        subBranch_1 = Branch("Can stop them winning it?", Leaf(
            "Goto stop Tree"), Leaf("Go back up this tree"))

        subsubsubBranch_2_1 = Branch("Does oldest card play priority beat my hate play priority?", Leaf(
            "Play old card"), Leaf("Play hate card"))  # TODO

        subsubBranch_2_1 = Branch(
            "Do I multiple playable cards?", subsubsubBranch_2_1, Leaf("Play a card"))

        subBranch_2 = Branch("Do I have playable cards?",
                             subsubBranch_2_1, Leaf("Do nothing"))

        start_Branch = Branch(
            "Is there an apparent winner?", subBranch_1, subBranch_2)

        self.Dec_Tree = start_Branch


def test_Main_Decision_Tree:
    test = Main_Decision_Tree("test", 2)

    test.gen_Dec_Tree()

    level_0 = test.Dec_Tree

    (level_1_L, level_1_R) = test.Dec_Tree.get_offshoots()

    (level_2_1_L_L, level_2_1_L_R) = level_1_L.get_offshoots()

    print(level_2_1_L_L.value)
    print(level_2_1_L_R.value)


def travel_Card_Guess_Tree(Card_Tree, max_depth):
    # list that will be appened card data in the format of
    # [(card1_color, depth), (card1_type, depth), (card2_color, depth)...]
    Card_Guess_list = []

    def travel_recus(Card_Tree, depth):
        (left_tree, right_tree) = read_Card_Tree_basic(Card_Tree)
         # case were no card is at this level of memory just return
        if left_tree is None and right_tree is None:
            return None
            pass
        # get this levels card data (color and type)
        (Card_color_p, Card_Type_p) = read_Card_Tree_values(right_tree)
        Card_Guess_list.append(Card_color_p)
        Card_Guess_list.append(Card_Type_p)

        # go to the next level of Card_Guess_Tree which is in the left_tree
        travel_recus(left_tree, depth + 1)

        return None

    travel_recus(Card_Tree, 0)
    slice_num = None

    # find the point in Card_Guess_list where the maximum depth is passed
    for i in range(len(Card_Guess_list)):
        (card_data, depth) = Card_Guess_list[i]
        if depth > max_depth:
            slice_num = i
            break
            
    # if the maximum depth is passed slice the Card_Guess_list at this point
    if not (slice_num is None):
        Card_Guess_list[:slice_num:]
    else:
        pass

    # list that will be appended pairs of the card_data (both the color and
    # type), note unlike Card_Guess_list depth data is removed.
    # The format is as follows (eg 3 max depth) [(card1_color, card1_type),
    # (card2_color, card2_type), (card3_color, None)]
    output_list = []

    # filter out the depth values for clean output and pair color and
    # type together
    for i in range(0, len(Card_Guess_list), 2):  # TODO FIXISH
        (card_data_1, depth_1) = Card_Guess_list[i]
        (card_data_2, depth_2) = Card_Guess_list[i + 1]

        output_list.append((card_data_1, card_data_2))

    # if Card_Guess_list was odd above code would miss the last cards first
    # data value do to range iterating by 2
    if not len(Card_Guess_list) % 2 == 0:
        (card_data_1, depth_1) = Card_Guess_list[-1]
        output_list.append((card_data_1, None))

    return output_list



def read_Card_Tree_values(Card_Tree, depth):
    (Card_color, Card_Type) = Card_Tree.get_offshoots()
    return ((Card_color.value, depth), (Card_Type.value, depth + 1))


def read_Card_Tree_basic(Card_Tree):
    (left_tree, right_tree) = Card_Tree.get_offshoots()
    return (left_tree, right_tree)


class Card_Guess_Tree:
    def __init__(self, name, max_depth=0):
        self.name = name
        self.Card_Tree = None
        self.max_depth = max_depth

    def gent_Card_Tree(self):
        start_Branch = Branch()
        self.Card_Tree = start_Branch

    def read_card_tree(self):
        pass

    def update_card_tree(self, card):
        Card_Tree = self.Card_Tree
        card_Branch = Branch(card.color, card.type)
        # add new card at new top of Card_Guess_Tree
        self.Card_Tree = Branch(None, Card_Tree, card_Branch)

        # other bottom append method
        # def travel_Card_Guess_Tree_end(Card_tree, card_Branch):
        #         (left_tree, right_tree) = read_Card_Tree_basic(Card_Tree)
        #         if left_tree is None and right_tree is None:  # case were no card is at this level of memory add new card data
        #             left_tree = Branch(None, None, card_Branch)
        #             return None
        #         travel_Card_Guess_Tree_end(left_tree, card_Branch)
        #         return None

        # travel_Card_Guess_Tree_end(Card_Tree, card_Branch)


        pass

def  test_Card_Guess_Tree():
        test_tree = Card_Guess_Tree("test", 3)
