import twttr

def main():
    test_shorten()

def test_shorten():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("tw'tter") == "tw'ttr"
    assert twttr.shorten("twttr") == "twttr"
    assert twttr.shorten("twitter twitter") == "twttr twttr"
    assert twttr.shorten("Tw'tter") == "Tw'ttr"
    assert twttr.shorten("twt2tr") == "twt2tr"
    assert twttr.shorten("tw,tter") == "tw,ttr"
    assert twttr.shorten("twIttEr") == "twttr"



if __name__ == "__main__":
    main()