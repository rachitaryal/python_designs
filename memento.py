class State:
    """ this is "memento" class / it determines the object state """

    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content