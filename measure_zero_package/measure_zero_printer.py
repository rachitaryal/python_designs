from measure_zero_package.base.measure_zero_printer_base import MeasureZeroPrinterBase
from measure_zero_package.measure import MeasureExecutionTime, MeasureSize


class MeasureZeroExecTime(MeasureZeroPrinterBase):

    def __init__(self, fn, *fn_args, **fn_kwargs):
        super().__init__(fn, *fn_args, **fn_kwargs)
        self.m_exec_time = MeasureExecutionTime(fn, *fn_args, **fn_kwargs)

    def _default(self):
        exec_time = self.m_exec_time.measure()
        print(f"[{self.fn.__name__}] took {exec_time} secs to execute.")


class MeasureZeroSize(MeasureZeroPrinterBase):

    def __init__(self, fn, *fn_args, **fn_kwargs):
        super().__init__(fn, *fn_args, **fn_kwargs)
        self.m_size = MeasureSize(fn, *fn_args, **fn_kwargs)

    def _default(self):
        size = self.m_size.measure()
        if not size:
            print(f"[{self.fn.__name__}] doesn't return any data.")
            return
        print(f"[{self.fn.__name__}] returns {size} bytes of data.")
