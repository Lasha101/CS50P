import random
import sys
def main():
    generate_integer(get_level())

def get_level():
    while True:
        n = input("Level:")
        if n == "1" or n == "2" or n == "3":
            return int(n)
        else:
            continue
def generate_integer(level):
    j = 0
    counter = 0
    if level == 1:
        from_digit = 0
        before_digit = 9
    elif level == 2:
        from_digit = 10
        before_digit = 99
    else:
        from_digit = 100
        before_digit = 999
    for i in range(10):
        x = random.randint(from_digit, before_digit)
        y = random.randint(from_digit, before_digit)
        for k in range(3):
            z = input(str(x) + " + " + str(y) + " = ")
            try:
                if int(z) == x + y:
                    j += 1
                    break
                else:
                    counter += 1
                    print("EEE")
                    if counter == 3:
                        print(f"{x} + {y} = {x + y}")
            except ValueError:
                print("EEE")
                pass
    print(f"Score: {j}")
    sys.exit()

if __name__ == "__main__":
    main()
