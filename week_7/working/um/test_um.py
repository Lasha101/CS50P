import pytest
from um import count

def main():
    test_input()

def test_input():
    assert count("Um, i wanted this album.") == 1
    assert count("um?") == 1
    assert count("Um, it's better, um...") == 2
    assert count("Um") == 1


if __name__ == "__main__":
    main()