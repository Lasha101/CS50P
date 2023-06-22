def main():
    s = input("Input:")
    print("Output:", shorten(s))

def shorten(word):
    letters = []
    for i in word:
        match i:
            case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
                i = i.replace(i, "")
            case _:
                letters.append(i)
    new_s = "".join(letters)
    return new_s


if __name__ == "__main__":
    main()