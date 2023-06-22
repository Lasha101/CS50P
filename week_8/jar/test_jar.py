
from jar import Jar
import pytest
def main():
    test_withdraw()
    test_deposit()
    test_init()
    test_str()



def test_init():
    jar = Jar(10)

    assert jar._capacity == 10
    assert jar._size == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar(10)
    # if jar._size == 7:
    #     assert jar.withdraw(7) == 0
    #     assert jar.withdraw(3) == 4
    # with pytest.raises(ValueError):
    #     jar = Jar(-1)
    #     jar = Jar("cat")
    jar.deposit(8)
    with pytest.raises(ValueError):
        jar.withdraw(9)
    assert jar.withdraw(2) == 6
    assert jar.withdraw(5) == 1



def test_deposit():

    jar = Jar(10)
    obj = Jar()
    assert jar.deposit(10) == 10
    with pytest.raises(ValueError):
        obj.deposit(15)
        jar = Jar(-1)
        jar = Jar("cat")


if __name__ == "__main__":
    main()