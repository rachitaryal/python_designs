from sys import getsizeof
from time import time
from abc import ABC, abstractmethod


class ListOfTupleError(Exception):
    pass


class MeasureZeroDataBase(ABC):
    """
         All the methods in the class returns the actual data.
         If you want to just print the calculation on the terminal use MeasureZero class implemented using MeasureZeroBase class
    """

    def __init__(self, fn, *fn_args, **fn_kwargs):
        self.fn = fn
        self.fn_args = fn_args
        self.fn_kwargs = fn_kwargs

    def _run_func(self):
        """ method to execute the function along with the args or kwargs passed """
        data = self.fn(*self.fn_args, **self.fn_kwargs)
        return data

    @abstractmethod
    def get_exec_time(self):
        """ method to measure the execution time for the function """
        pass

    @abstractmethod
    def get_size(self):
        """ method to measure the size of data returned by the function """
        pass

    @abstractmethod
    def get_all(self):
        """ method to measure all the methods i.e. measure_size() and measure_exec_time() """
        pass


class MeasureZeroData(MeasureZeroDataBase):

    def get_exec_time(self):
        """ method to measure the execution time for the function """
        begin = time()
        data = self._run_func()
        end = time()
        exec_time = end - begin
        return exec_time

    def get_size(self):
        """ method to measure the size of data returned by the function """
        data = self._run_func()
        if data:
            size = getsizeof(data)
            return size

    def get_all(self):
        """ method to measure all the methods i.e. measure_size() and measure_exec_time() """
        return self.get_size(), self.get_exec_time()


class MeasureZeroBase(ABC):
    """
        Methods in the class doesn't return data but prints the evaluated value in the terminal
        If you want to access the actual data use MeasureZeroData class implement using MeasureZeroDataBase class
    """

    def __init__(self, fn, *fn_args, **fn_kwargs):
        self.fn = fn
        self.measure = MeasureZeroData(fn, *fn_args, **fn_kwargs)

    @abstractmethod
    def measure_exec_time(self):
        """ method to measure the execution time for the function """
        pass

    @abstractmethod
    def measure_size(self):
        """ method to measure the size of data returned by the function """
        pass

    @abstractmethod
    def measure_all(self):
        """ method to measure all the methods i.e. measure_size() and measure_exec_time() """
        pass


class MeasureZero(MeasureZeroBase):

    def measure_exec_time(self):
        """ method to measure the execution time for the function """
        exec_time = self.measure.get_exec_time()
        print(f"[{self.fn.__name__}] took {exec_time} secs to execute.")

    def measure_size(self):
        """ method to measure the size of data returned by the function """
        size = self.measure.get_size()
        if not size:
            print(f"[{self.fn.__name__}] doesn't return any data.")
            return
        print(f"[{self.fn.__name__}] returns {size} bytes of data.")

    def measure_all(self):
        """ method to measure all the methods i.e. measure_size() and measure_exec_time() """
        self.measure_size()
        self.measure_exec_time()


class MeasureZeroManyBase(ABC):
    """
        ---> Class to implement evaluation on list of functions and their arguments
        ---> __init__ takes in methods=[] parameter; methods is list of tuples
                with each tuple containing function as first argument and function's parameters as second argument
                i.e. methods=[(func, args), (func, args), ...]
    """

    def __init__(self, methods=[]):
        self.methods = methods

    @abstractmethod
    def _default(self):
        pass

    def measure(self):
        """ method to execute default behaviour """
        self._default()


class MeasureZeroMany(MeasureZeroManyBase):
    """
            Class to evaluate measure_all() on multiple methods
    """

    def _default(self):
        if not all(isinstance(item, tuple) for item in self.methods):
            raise ListOfTupleError("Method should contain list of tuples.")

        if self.methods:
            for each in self.methods:
                if len(each) >= 2:
                    MeasureZero(each[0], each[1]).measure_all()
                else:
                    MeasureZero(each[0]).measure_all()


class MeasureZeroManyTime(MeasureZeroManyBase):
    """
        Class to evaluate measure_exec_time() on multiple methods
    """

    def _default(self):
        if not all(isinstance(item, tuple) for item in self.methods):
            raise ListOfTupleError("Method should contain list of tuples.")

        if self.methods:
            for each in self.methods:
                if len(each) >= 2:
                    MeasureZero(each[0], each[1]).measure_exec_time()
                else:
                    MeasureZero(each[0]).measure_exec_time()


class MeasureZeroManySize(MeasureZeroManyBase):
    """
        Class to evaluate measure_size() on multiple methods
    """

    def _default(self):
        if not all(isinstance(item, tuple) for item in self.methods):
            raise ListOfTupleError("Method should contain list of tuples.")

        if self.methods:
            for each in self.methods:
                if len(each) >= 2:
                    MeasureZero(each[0], each[1]).measure_size()
                else:
                    MeasureZero(each[0]).measure_size()


def mul(ls=[]):
    r_ls = [x * x for x in ls if ls]
    return r_ls


def mul2(ls=[]):
    r_ls = (x * x for x in ls if ls)
    return r_ls


def mul3(ls=[]):
    if ls:
        for x in ls:
            yield x * x


my_lst = []

for i in range(100000):
    my_lst.append(i)


# MeasureZero(mul, my_lst).measure_size()
# MeasureZero(mul, my_lst).measure_exec_time()

def test():
    val = []
    for x in range(100000):
        val.append(x)


methods_lst = [(mul, my_lst), (mul2, my_lst), (test,)]

MeasureZeroMany(methods_lst).measure()
