import time


class MyIterator:
    def __init__(self):
        self.iter_ = iter([1, 2, 3])
        self.i = False

    def __iter__(self, i=False):
        print("iter call")
        print("iter {}".format(i))
        self.i = i
        return self

    def __next__(self):
        print("next call")
        for i in self.iter_:
            return i

    def test(self):
        print("test call")
        for d in self.__iter__(True):
            time.sleep(1)
            print("test: {}".format(d))
            print("i: {}".format(self.i))
            if not d:
                break


print("MyIterator".center(100, "#"))
q = MyIterator()
q.test()


class MyIterable:
    def __init__(self):
        self.i = False

    def __iter__(self, i=False):
        print("outer iter call")
        for j in [1, 2, 3]:
            print("iter call")
            self.i = i
            print("iter {}".format(i))
            yield j

    def test(self):
        print("test call")
        for d in self.__iter__(True):
            time.sleep(1)
            print("test: {}".format(d))
            print("i: {}".format(self.i))


print("MyIterable".center(100, "#"))
q = MyIterable()
q.test()


class StrangeIterator:
    def __init__(self):
        self.iter_ = iter([1, 2, 3])
        self.i = False

    def __iter__(self, i=False):
        print("out iter call")
        time.sleep(1)
        for j in self.iter_:
            self.i = i
            print("iter call")
            print("iter {}".format(i))
            time.sleep(1)
            yield j

    def __next__(self):
        print("next call")
        for i in self.__iter__(True):
            time.sleep(1)
            return i


print("StrangeIterator".center(100, "#"))
strange_iterator = StrangeIterator()
for s in strange_iterator:
    print(s)
print("*" * 100)
strange_iterator = StrangeIterator()
for i in range(5):
    print(f"i: {i}")
    print(next(strange_iterator))


class LoopNext:
    def __init__(self):
        self.iter_ = iter([1, 2, 3])
        self.i = False

    def __iter__(self, i=False):
        print("out iter call")
        time.sleep(1)
        for j in self.iter_:
            self.i = i
            print("iter call")
            print("iter {}".format(i))
            time.sleep(1)
            yield j

    def __next__(self):
        print("next call")
        while True:
            for i in self.__iter__(True):
                time.sleep(1)
                return i


print("LoopNext".center(100, "#"))
loop_next = LoopNext()
for s in loop_next:
    print(s)
print("*" * 100)
loop_next = LoopNext()
for i in range(5):
    print(f"i: {i}")
    print(next(loop_next))


class AnotherStrangeIterator:
    def __init__(self):
        self.iter_ = iter([1, 2, 3])
        self.i = False

    def __iter__(self, i=False):
        print("out iter call")
        for j in [1, 2, 3]:
            self.i = i
            print("iter call")
            print("iter {}".format(i))
            time.sleep(1)
            yield j

    def __next__(self):
        print("next call")
        for i in self.__iter__(True):
            time.sleep(1)
            yield i


print("AnotherStrangeIterator".center(100, "#"))
strange_iterator = AnotherStrangeIterator()
for s in strange_iterator:
    print(s)
print("*" * 100)
strange_iterator = AnotherStrangeIterator()
for i in range(2):
    si = next(strange_iterator)
    print(si)
    for j in si:
        print(j)
