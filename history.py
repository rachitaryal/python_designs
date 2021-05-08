
class History:
    """ this is "care taker" class / it holds all the states """

    def __init__(self):
        self.history = []
        self.popped = []

    @staticmethod
    def __validate_state(state):
        if not type(State):
            raise Exception("Invalid state")
        return

    def add_state(self, state):
        self.__validate_state(state)
        if state not in self.history:
            self.history.append(state)

    def get_current_state(self):
        cs = self.history[-1]
        return cs

    def undo(self):
        if len(self.history) > 1:
            val = self.history.pop()
            self.popped.append(val)

    def redo(self):
        if len(self.popped):
            val = self.popped.pop()
            self.history.append(val)