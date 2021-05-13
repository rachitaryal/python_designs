from measure_zero_package.measure_zero import MeasureZero
from measure_zero_package.measure_zero_printer import MeasureZeroSize, MeasureZeroExecTime


def mul(ls=[]):
    r_ls = [x * x for x in ls if ls]
    return r_ls


def mul2(ls=[]):
    r_ls = (x * x for x in ls if ls)
    return r_ls


my_lst = []

for i in range(100000):
    my_lst.append(i)


# MeasureZero(mul, my_lst).measure_size()
# MeasureZero(mul, my_lst).measure_exec_time()

def test():
    val = []
    for x in range(10000000):
        val.append(x)


# MeasureZeroExecTime(mul, my_lst).measure()
# MeasureZeroSize(mul, my_lst).measure()


methods_lst = [(mul, my_lst), (mul2, my_lst), (test,)]

MeasureZero(tup_lst=methods_lst, cls=[MeasureZeroExecTime, MeasureZeroSize])
