from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2,3) == 5
    assert add(-2,-3) == -5

def test_subtract():
    assert subtract(2,3) == -1
    assert subtract(-2,-3) == 1

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(-2,-3) == 6
    assert multiply(5,0) == 0

def test_divide():
    assert divide(6,2) == 3
    assert divide(6,0) == "invalid!"