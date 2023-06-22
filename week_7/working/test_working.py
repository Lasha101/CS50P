import pytest
from working import convert

def main():
    test_convert()
    test_value_error()

def test_convert():
    assert convert("10 AM to 6 PM") == "10:00 to 18:00"
    assert convert("10:00 AM to 6:00 PM") == "10:00 to 18:00"
    assert convert("9 PM to 7 AM") == "21:00 to 07:00"
    assert convert("11:30 PM to 9:50 AM") == "23:30 to 09:50"

def test_value_error():
    with pytest.raises(ValueError):
        convert("10AM - 6PM")
    with pytest.raises(ValueError):
        convert("10:00 to 18:00")
    with pytest.raises(ValueError):
        convert("16:00 AM to 26:00 PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

if __name__ == "__main__":
    main()