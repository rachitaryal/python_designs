from measure_zero_package.base.measure_zero_base import MeasureZeroBase
from measure_zero_package.dispatcher import DispatchMain


class MeasureZero(MeasureZeroBase):

    def __init__(self, tup_lst=[], cls=[], dispatch_cls=DispatchMain, *args, **kwargs):
        print("\n::: MeasureZero Start :::\n")
        self.dispatch_ins = dispatch_cls(tup_lst=tup_lst, cls=cls, *args, **kwargs)
        self.dispatch_ins.run()
        print("\n::: MeasureZero End :::\n")