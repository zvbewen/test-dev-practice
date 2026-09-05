import pytest
def add(a,b):
    return a + b
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
def test_sub():
    assert 3 - 1 == 2 
def multiply(a,b):
    return a*b
def test_multiply():
    assert multiply(2,3) ==  6
def test_assert_family():
    assert add(2,3) == 5, f"add(2,3)应该等于6，但实际是{add(2,3)}"
    assert add(2,3) != 7
    assert [1,2,3]
    assert "pytest" in ["pytest", "unittest"]
    assert 10 > 3
    assert None is None
def divide(a,b):
    if b == 0 :
        raise ValueError("除数不能为 0")
    return a / b
def test_divide_normal():
    assert divide(10,2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
