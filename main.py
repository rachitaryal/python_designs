import functools
from sys import getsizeof
from time import time


def time_it(fn):
    """
        returns the (data, time) tuple
        data is the actual data returned by the function
        time is the execution time for the function
    """

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        begin = time()
        data = fn(*args, **kwargs)
        end = time()
        exec_time = end - begin
        print(f"Function '{fn.__name__}()' took {exec_time} secs to execute.")
        return data, exec_time

    return wrapper


def size_it(fn):
    """
        returns the (data, size) tuple
        data is the actual data returned by the function
        size is the bytes size returned by the function
    """

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        size = getsizeof(data)
        print(f"Function '{fn.__name__}()' returns {size} bytes of data.")
        return data, size

    return wrapper


def sajau(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        fn(*args, **kwargs)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    return wrapper



@sajau
@time_it
# @size_it
def test(a, b, c):
    return [x for x in range(100000)]


test(1, 2, 3)
