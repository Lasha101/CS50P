import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Define the regular expression pattern to match the word "um" surrounded by non-word characters or the start/end of the string
    reg_ex = "(^|\W)um($|\W)"

    # Find all matches of the pattern in the given string, ignoring case sensitivity
    matching = re.findall(reg_ex, s, re.IGNORECASE)

    # If matches are found, return the count of matches
    if matching:
        return len(matching)

    # If no matches are found, return 0
    return 0

if __name__ == "__main__":
    main()