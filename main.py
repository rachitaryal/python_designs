from observers import ObserverFirst, ObserverSecond, ObserverThird
from publisher import Publisher
if __name__ == '__main__':
    s1 = ObserverFirst()
    s2 = ObserverSecond()
    s3 = ObserverThird()

    p = Publisher()
    p.subscribe(s1)
    p.subscribe(s2)
    p.subscribe(s3)

    # p.unsubscribe(s2)

    p.run()