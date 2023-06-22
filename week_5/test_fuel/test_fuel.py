import fuel
import pytest
from fuel import convert
def main():
    test_convert()
    test_gauge()
    test_zero_division()
    test_value_error()
    test_value_error_2()

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("2/3") == 67
    assert fuel.convert("1/3") == 33

def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(0.01) == "E"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(25) == "25%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("4/0")
        convert("10/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("a/b")
        convert(" ")
        convert("gdgro fsd")

def test_value_error_2():
    with pytest.raises(ValueError):
        convert("15/3")
        convert("2/1")
        convert("6/3")


if __name__ == "__main__":
    main()