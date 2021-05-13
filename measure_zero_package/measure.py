from measure_zero_package.base.measure_base import MeasureBase
from sys import getsizeof
from time import time


class MeasureSize(MeasureBase):

    def _default(self):
        data = self._run_func()
        if data:
            size = getsizeof(data)
            return size


class MeasureExecutionTime(MeasureBase):

    def _default(self):
        begin = time()
        data = self._run_func()
        end = time()
        exec_time = end - begin
        return exec_time
