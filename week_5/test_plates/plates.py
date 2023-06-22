def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid", end="\n")
    else:
        print("Invalid", end="\n")

def length(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        return True
    return False

def str_alnum(s):

    for i in range(len(s) - 1):
        if s[i].isnumeric() and s[i + 1].isalpha():
            return False
    return True


def no_firstzero(s):

    for i in range(len(s)):
        if i > 1 and s[i] == "0" and s[i - 1].isalpha():
            return False
    return True

def is_alnum(s):
    return s.isalnum()


def is_valid(s):
    if length(s) and str_alnum(s) and no_firstzero(s) and is_alnum(s):
        return True
    return False


if __name__ == "__main__":
    main()
