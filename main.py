from memento import State
from history import History
from originator import Content

if __name__ == '__main__':
    print("______MEMENTO PATTERN______")
    h = History()
    s1 = State("State one content")
    s2 = State("State two content")
    s3 = State("State three content")

    h.add_state(s1)
    h.add_state(s2)
    h.add_state(s3)

    h.undo()
    h.undo()
    h.undo()
    h.undo()
    h.undo()
    h.redo()
    h.redo()
    h.redo()
    h.redo()
    h.redo()
    h.undo()
    current_state = h.get_current_state()
    current_content = Content(current_state)
    print(current_content.get_content())
