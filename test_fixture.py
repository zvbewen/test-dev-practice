import pytest 

def subtract(a,b):
    return a - b

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

@pytest.fixture
def sample_numbers():
    return (10, 5)

def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_subtract_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5

def test_multiply_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 50

@pytest.fixture
def log_fixture():
    print("\n[setup] 准备开始")
    yield "准备好了"
    print("\n[teardown] 清理结束")

def test_order(log_fixture):
    print("\n[测试中] 收到:", log_fixture)
    assert log_fixture == "准备好了"

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
    (-5, -3, -8),
    (7, 0, 7),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected