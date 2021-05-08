# Memento Pattern

###### The memento pattern is a software design pattern that provides the ability to restore an object to its previous state (undo via rollback).

![](images/gif/memento_pattern.gif)

## What problems can the Memento design pattern solve?

- The internal state of an object should be saved externally so that the object can be restored to this state later.
- The object's encapsulation must not be violated.

The memento pattern is implemented with three objects: the originator, a caretaker and a memento. The originator is some object that has an internal state. The caretaker is going to do something to the originator, but wants to be able to undo the change. The caretaker first asks the originator for a memento object. Then it does whatever operation (or sequence of operations) it was going to do. To roll back to the state before the operations, it returns the memento object to the originator. The memento object itself is an opaque object (one which the caretaker cannot, or should not, change). When using this pattern, care should be taken if the originator may change other objects or resources—the memento pattern operates on a single object.

> What but design of darkness to appall?
> If design govern in a thing so small.
> — Frost Robert

Now let's see how Mememto Pattern is implemented

## Implementation

#### Step 1:

###### memento.py

---

```sh
class State:
    """ this is 'memento' class / it determines the object state """

    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content
```

#### Step 2:

###### history.py

---

```sh

class History:
    """ this is 'care taker' class / it holds all the states """

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
```

#### Step 3:

###### originator.py

---

```sh
class Content:
    """
        - this is "originator" class / this class accepts the state to work upon
        - accepts the instance of state class
    """

    def __init__(self, state):
        self.state = state

    def get_content(self):
        return self.state.get_content()

```

#### Step 4:

###### main.py

---

```sh
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

```

### Conclusion

###### Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.
