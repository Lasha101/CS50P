def main():
    print_fuel_in_tank(fuel_percent())

def fuel_percent():
    while True:
        try:
            enter_fraction = input("Fraction:")
            x, y = enter_fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            elif y == 0:
                continue
        except ValueError:
            continue
        else:
            result = round((x/y) * 100)
            return result

def print_fuel_in_tank(percent):
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(str(percent) + "%", end="")

main()







