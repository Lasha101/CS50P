def main():
    print_output_string(consonant_string(string_without_voyels(user_input())))

def user_input():
    s = input("Input:")
    return s

def string_without_voyels(s):
    letters = []
    for i in s:
        match i:
            case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
                i = i.replace(i, "")
            case _:
                letters.append(i)
    return letters

def consonant_string(s):
    new_s = "".join(s)
    return new_s

def print_output_string(s):
    print("Output:", s)

if __name__ == "__main__":
    main()