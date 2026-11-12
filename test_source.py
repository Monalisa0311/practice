from source import add
import pytest

@pytest.mark.parametrize("*numbers, sum", 
    [((10, 20), 30),
     ((10, 60), 30),
    ((10, 20, 30), 60),
    ((10, 20, 30, 40), 100),
    ((-10, 20, 30), 40),
    ((0, 0, 0), 0)
    ])

def test_one(numbers,sum):
    assert add(*numbers)==sum