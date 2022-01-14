class A:
    def __init__(self):
        self.dict_data = {"a": 0, "b": 1, "c": 2}
        self.list_data = [0, 1, 2]

    def __getitem__(self, key):
        print(key)
        if isinstance(key, str):
            print("str")
            return self.dict_data[key]
        elif isinstance(key, int):
            print("int")
            return self.list_data[key]
        print("not found")


a = A()
print("1".center(20, "#"))
print(a["a"])
print("2".center(20, "#"))
print(a[1])
print("3".center(20, "#"))
print(1 in a)
print("4".center(20, "#"))
print("a" in a)
print("5".center(20, "#"))
for i in a:
    print(i)
"""
当定义了__getitem__， 没有定义__contain_的时候
以key或者index检索元素时候, 会调用__getitem__方法
以in 形式检索时, 每次传入从0开始一次增长, 返回的值相符为True
直到产生IndexError，值为False
for 方法类似, 从0开始循环, 直到碰见IndexError
#########1##########
a
str
0
#########2##########
1
int
1
#########3##########
0
int
1
int
True
#########4##########
0
int
1
int
2
int
3
int
False
#########5##########
0
int
0
1
int
1
2
int
2
3
int
"""


class A1:
    def __init__(self):
        self.dict_data = {"a": 0, "b": 1, "c": 2}
        self.list_data = [0, 1, 2]

    def __getitem__(self, key):
        print(key)
        if isinstance(key, str):
            print("str")
            return self.dict_data[key]
        elif isinstance(key, int):
            print("int")
            raise IndexError
            return self.list_data[key]
        print("not found")


a = A1()
print("*" * 20)
print(1 in a)
print("*" * 20)
for i in a:
    print(i)
"""
********************
0
int
False
********************
0
int
"""


class B:
    def __init__(self):
        self.dict_data = {"a": 0, "b": 1, "c": 2}
        self.list_data = [0, 1, 2]

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.dict_data[key]
        elif isinstance(key, int):
            raise IndexError
            return self.list_data[key]

    def __contain__(self, key):
        if isinstance(key, str):
            return False
        else:
            return True


b = B()
print("@" * 20)
print("a" in b)
print(1 in b)
print("@" * 20)
for i in b:
    print(i)
"""
@@@@@@@@@@@@@@@@@@@@
False
False
@@@@@@@@@@@@@@@@@@@@
"""
