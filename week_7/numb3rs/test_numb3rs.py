from numb3rs import validate


def test_validate():
    # Assert that "123.32" is not a valid IPv4 address
    assert validate("123.32") == False

    # Assert that "1.2.3.4" is a valid IPv4 address
    assert validate("1.2.3.4") == True

    # Assert that "127.0.0.1" is a valid IPv4 address
    assert validate("127.0.0.1") == True

    # Assert that "249.249.249.249" is a valid IPv4 address
    assert validate("249.249.249.249") == True

    # Assert that "1.2.3.1000" is not a valid IPv4 address
    assert validate("1.2.3.1000") == False

    # Assert that "hey.you.cat.dog" is not a valid IPv4 address
    assert validate("hey.you.cat.dog") == False

    # Assert that "hi" is not a valid IPv4 address
    assert validate("hi") == False

    # Assert that "255.255.255.255" is a valid IPv4 address
    assert validate("255.255.255.255") == True

    # Assert that "11.99.22.88" is a valid IPv4 address
    assert validate("11.99.22.88") == True

    # Assert that "199.911.288.882" is not a valid IPv4 address
    assert validate("199.911.288.882") == False

    # Assert that "256.256.256.256" is not a valid IPv4 address
    assert validate("256.256.256.256") == False







