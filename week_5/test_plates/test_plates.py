import plates

def main():
    test_is_valid()

def test_is_valid():
    assert plates.is_valid("Abs045") == False
    assert plates.is_valid("Ab") == True
    assert plates.is_valid("Ab44b5") == False
    assert plates.is_valid("Ab4-45") == False
    assert plates.is_valid("Ab445") == True
    assert plates.is_valid("Ab44445") == False
    assert plates.is_valid("12445") == False

if __name__ == "__main__":
    main()
