class cell(object):

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        if state != 0 or state !=1:
            die("Enter 0 or 1!")

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        if state != 0 and state != 1:
            die("Enter 0 or 1!")

def test_cell():
