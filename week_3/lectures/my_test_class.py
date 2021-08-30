from collections import Counter


def test_counter1():
    c = Counter()
    c.update({'tja': 5})
    assert c['tja'] == 5


def test_counter2():
    c = Counter()
    c.update({'tja': 5})
    assert c['tja'] == 6


class TestClass:

    def setup(self):
        self.c = Counter()

    def test_1(self):
        self.c.update({'tja': 5})
        assert self.c['tja'] == 5

    def test_2(self):
        assert self.c['tja'] == 5

    def test_3(self):
        assert self.c['tja'] == 0

