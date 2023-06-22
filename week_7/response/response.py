import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(e):
    if validators.email(e) == True:
        return f"Valid"
    return f"Invalid"


if __name__ == "__main__":
    main()