from collections import Counter

def func(x):
    return x + 1

# def test_func2():
#     func('hej')

# def test_func():
#     assert func(3) == 5

# def test_fucn3():
#     assert func(3) == 5


# class TestClass:

#     def setup(self):
#         self.c = Counter()

#     def test_1(self):
#         self.c.update({'tja': 5})
#         assert self.c['tja'] == 5

#     def test_2(self):
#         assert self.c['tja'] == 5

#     def test_3(self):
#         assert self.c['tja'] == 0

def test_1():
    c = Counter()
    c.update({'tja': 5})
    assert c['tja'] == 5

def test_2():
    c = Counter()
    c.update({'tja': 5})
    assert c['tja'] == 6