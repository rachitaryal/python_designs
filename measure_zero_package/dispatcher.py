from measure_zero_package import TupleListError
from measure_zero_package.base.dispatcher_base import DispatchBase


class DispatchMain(DispatchBase):

    def validate(self):
        """ validate the tup_lst is list of tuples """
        if not all(isinstance(item, tuple) for item in self.tup_lst):
            raise TupleListError("Method should contain list of tuples.")
        return

    def _defualt(self):
        self.validate()
        if self.tup_lst and self.cls:
            for x in self.tup_lst:
                for CLS in self.cls:
                    if len(x) >= 2:
                        CLS(x[0], x[1]).measure()
                    else:
                        CLS(x[0]).measure()
