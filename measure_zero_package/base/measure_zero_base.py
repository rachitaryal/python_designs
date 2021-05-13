from abc import ABC, abstractmethod

from measure_zero_package.dispatcher import DispatchMain


class MeasureZeroBase(ABC):
    """
            Role: "Abstract Base Class"
            Responsibility: ["Execute the Dispatch Class"]
            Methods: {

            }
            AbstractMethods: {
                "__init__" : [
                        "takes the required args and kwargs",
                        "dispatches the dispatch_cls"
                ],
            }
    """

    @abstractmethod
    def __init__(self, tup_lst=[], cls=[], dispatch_cls=DispatchMain, *args, **kwargs):
        """ DispatchMain is the default dispatcher_cls """
        pass








