

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

        subBranch_1 = Branch("Can stop them winning it?", Leaf("Goto stop Tree"), Leaf("Go back up this tree"))

        subsubsubBranch_2_1 = Branch("Does oldest card play priority beat my hate play priority?", Leaf("Play old card"), Leaf("Play hate card")) #TODO

        subsubBranch_2_1 = Branch("Do I multiple playable cards?", subsubsubBranch_2_1, Leaf("Play a card"))

        subBranch_2 = Branch("Do I have playable cards?", subsubBranch_2_1, Leaf("Do nothing"))

        start_Branch = Branch("Is there an apparent winner?", subBranch_1, subBranch_2)

        self.Dec_Tree = start_Branch




def test_Main_Decision_Tree:
    test = Main_Decision_Tree("test", 2)

    test.gen_Dec_Tree()

    level_0=test.Dec_Tree

    (level_1_L, level_1_R)=test.Dec_Tree.get_offshoots()

    (level_2_1_L_L, level_2_1_L_R) = level_1_L.get_offshoots()

    print(level_2_1_L_L.value)
    print(level_2_1_L_R.value)
