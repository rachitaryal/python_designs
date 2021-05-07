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
