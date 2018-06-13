

class Leaf:
    def __init__(self, value):
        self.value = value


class Branch:
    def __init__(self, Branch_q=None, child_1=None, child_2=None):
        self.child_1 = child_1
        self.child_2 = child_2
        self.question = Branch_q

    def get_offshoots(self):
        """
        Returns a tuple of a branches two childs in order (child_1, child_2).
        """
        return (self.child_1, self.child_2)
