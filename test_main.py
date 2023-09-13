from main import add

def test_add_positive_numbers():
    result = add(3, 5)
    assert result == 8

def test_add_negative_numbers():
    result = add(-3, -5)
    assert result == -8

def test_add_mixed_numbers():
    result = add(3, -5)
    assert result == -2

def test_add_zero():
    result = add(0, 5)
    assert result == 5

def test_add_large_numbers():
    result = add(1000000, 2000000)
    assert result == 3000000
