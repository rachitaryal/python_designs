class Content:
    """
        - this is "originator" class / this class accepts the state to work upon
        - accepts the instance of state class
    """

    def __init__(self, state):
        self.state = state

    def get_content(self):
        return self.state.get_content()