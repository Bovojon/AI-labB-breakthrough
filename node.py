class Node:
    def __init__(self):
        self.parent = None
        self.children = []
        self.action = None
        self.state = None
        self.utility = None

    def is_terminal(self):
        if len(self.children) == 0:
            return True
        else:
            return False
