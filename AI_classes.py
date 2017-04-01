

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
    Card_Guess_list = []

    def travel_recus(Card_Tree, depth):
        (left_tree, right_tree) = read_Card_Tree_basic(Card_Tree)

        if left_tree is None and right_tree is None:  # case were no card is at this level of memory
            return None
            pass

        (Card_color_p, Card_Type_p) = read_Card_Tree_values(right_tree)
        Card_Guess_list.append(Card_color_p)
        Card_Guess_list.append(Card_Type_p)

        travel_recus(Caleft_tree, depth + 1)

        return None

    travel_recus(Card_Tree, 0)
    slice_num = None

    for i in range(len(Card_Guess_list)):
        (card_data, depth) = Card_Guess_list[i]
        if depth > max_depth:
            slice_num = i
            break

    if not (slice_num is None):
        Card_Guess_list[:slice_num:]
    else:
        pass

    output_list = []
    for i in range(0, len(Card_Guess_list), 2):  # TODO FIXISH
        (card_data_1, depth_1) = Card_Guess_list[i]
        (card_data_2, depth_2) = Card_Guess_list[i + 1]

        output_list.append([card_data_1, card_data_2])

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

    def read_card_tree(self):
        pass

    def update_card_tree(self, card):
