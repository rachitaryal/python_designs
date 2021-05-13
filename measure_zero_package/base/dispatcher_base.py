from abc import ABC, abstractmethod

from measure_zero_package import TupleListError


class DispatchBase(ABC):
    """
            Role: "Abstract Base Class"
            Responsibility: ["Dispatch the run method"]
            Methods: {
                "__init__" : "takes the required args and kwargs",
                "run" : "calls the _default method",
            }
            AbstractMethods: {
                "_default" : "determines the behaviour of the DispatchBase subclass"
            }
    """

    def __init__(self, tup_lst=[], cls=[], *args, **kwargs):
        self.tup_lst = tup_lst
        self.cls = cls

    @abstractmethod
    def _defualt(self):
        pass

    def run(self):
        return self._defualt()

