class Publisher:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer_cls):
        if observer_cls not in self.observers:
            self.observers.append(observer_cls)

    def unsubscribe(self, observer_cls):
        if observer_cls in self.observers:
            self.observers.remove(observer_cls)

    def run(self):
        if self.observers:
            for each in self.observers:
                each.call()
