
def test_1():
    assert False

def test_2():
    assert True

def test_3():
    x = 5 / 0

def test_4():
    raise NotImplementedError

def test_5():
    l = [5, 15, 100]
    assert max(l) == 100


# 
def increment(x):
    return x + 1


# def improved_increment(x):
#     try:
#         return x + 1
#     except Exception as e:
#         print(e)
        

def test_string_input():
    increment('hej')

def test_func():
    assert increment(3) == 5

def test_fucn3():
    assert increment(3) == 5