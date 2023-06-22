def main():
    f = input("Fraction:")
    print(gauge(convert(f)))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError
            percentage = round((x/y) * 100)
            return percentage
        except ValueError:
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{str(percentage)}%"

if __name__ == "__main__":
    main()