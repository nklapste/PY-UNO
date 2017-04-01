class Tree_base:
    def __init__(self):
        self.child = []

class Leaf:
    def __init__(self, value):
        self.value = value


class branch:
    def __init__(self, child1=None, child2=None):
        self.child1 = child1
        self.child2 = child2
