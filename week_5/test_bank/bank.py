def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}", end="")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        x = 0
    elif greeting[0] == "h":
        x = 20
    else:
        x = 100
    return x
if __name__ == "__main__":
    main()