from abc import ABC, abstractmethod


class MeasureBase(ABC):
    """
        Role: "Abstract Base Class"
        Responsibility: ["Return evaluated data"]
        Methods: {
            "__init__" : "takes the required args and kwargs",
            "measure" : "calls the _default method",
            "_run_func" : " executes the function with arguments passed ",
        }
        AbstractMethods: {
            "_default" : "determines the behaviour of the MeasureBase subclass"
        }
    """

    def __init__(self, fn, *fn_args, **fn_kwargs):
        self.fn = fn
        self.fn_args = fn_args
        self.fn_kwargs = fn_kwargs

    def _run_func(self):
        data = self.fn(*self.fn_args, **self.fn_kwargs)
        return data

    @abstractmethod
    def _default(self):
        pass

    def measure(self):
        return self._default()
