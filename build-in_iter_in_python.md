WHEN is build-in `__iter__` called  
WHAT hanppens `__iter__` is called mananully?  
WHAT happens if `__iter__` has additional arguments?  

https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
# code

```
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
                print("#" * 100)
                break


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


q = MyIterable()
q.test()
```

# result
```
$py iter.py
test call
iter call
iter True
iter call    # question: why does this three line output
iter False   # why is __iter__ called again
next call    #
test: 1
i: False     # for d in self.__iter__(True)
next call    # why does python ignore param True
test: 2      # The Value of i is always False
i: False
next call
test: 3
i: False
next call
test: None
i: False
####################################################################################################
test call
outer iter call
iter call
iter True
test: 1
i: True
iter call
iter True
test: 2
i: True
iter call
iter True
test: 3
i: True
```

# answer

In class MyIterator, function test is same as
```
def test(self):
    print("test call")
    it = self.__iter__(True)
    for d in it:
        time.sleep(1)
        print("test: {}".format(d))
        print("i: {}".format(self.i))
```
When `it = self.__iter__(True)` is excecuted, output is 
```
iter call
iter True
```
and return an iterator.
Then came to `for d in it`
when a python's iterator is first iterated, it calls build-in `__iter__`, and when calling 
build-in `__iter__`, caller doesn't give any additional arguments, but an defualt value False is set in `def __iter__(self, i=False)`, so python does not raise an Exception and the value of `i` is always False. 
read https://stackoverflow.com/questions/43519285/does-for-loop-call-iter

As for `MyIterable`, function `__iter__` provides a generator, code is hanged after `yield`, and begin with `for j in [1, 2, 3]` in the next loop of `for d in self.__iter__(True)`, so `print("outer iter call")` is only called once and code in `for j in [1, 2, 3]` is called for 3 times. 
