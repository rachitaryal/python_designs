# Observer Pattern (Pub Sub Pattern)

###### The observer pattern is a software design pattern in which an object, named the publisher, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

![](images/gif/observer_pattern.gif)

## Features

- It supports the principle of loose coupling between objects that interact with each other.
- It allows sending data to other objects effectively without any change in the Publisher or Observer classes.
- Observers can be added/removed at any point in time.

Observer pattern uses two actor classes viz: Publisher and Observer. There could also be a third class which uses the above mentioned classess. But primarily we consider two class Publisher and Observers. Publisher is an object having methods to attach and detach observers to a client object. We have created an abstract class IObserver and it's concrete class implementations that is extending class IObserver.

> What but design of darkness to appall?
> If design govern in a thing so small.
> — Frost Robert

Now let's see how Pub Sub is implemented

## Implementation

#### Step 1:

###### publisher.py

---

```sh
class Publisher:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer_cls):
        if observer_cls not in self.observers:
            self.observers.append(observer_cls)

    def unsubscribe(self, observer_cls):
        if observer_cls in self.observers:
            self.observers.remove(observer_cls)

    def run(self):
        if self.observers:
            for each in self.observers:
                each.call()

```

#### Step 2:

###### observers.py

---

```sh
from abc import ABC, abstractmethod


class IObserver(ABC):
    """ this is just an interface of observer """

    @abstractmethod
    def call(self):
        """ abstract method that need to be implemented in all the subclass """
        pass


class ObserverFirst(IObserver):

    def call(self):
        print("Observer First ran...")


class ObserverSecond(IObserver):

    def call(self):
        print("Observer Second ran...")


class ObserverThird(IObserver):

    def call(self):
        print("Observer Third ran...")


```

#### Step 3:

###### main.py

---

```sh
from observers import ObserverFirst, ObserverSecond, ObserverThird
from publisher import Publisher
if __name__ == '__main__':
    s1 = ObserverFirst()
    s2 = ObserverSecond()
    s3 = ObserverThird()

    p = Publisher()
    p.subscribe(s1)
    p.subscribe(s2)
    p.subscribe(s3)

    # p.unsubscribe(s2)

    p.run()

```

### Conclusion

###### The observer pattern is used when: the change of a state in one object must be reflected in another object without keeping the objects tight coupled. the framework we are writing needs to be enhanced in future with new observers with minimal changes.
