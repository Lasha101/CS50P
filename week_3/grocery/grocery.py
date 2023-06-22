def main():
    print_fruits()

def print_fruits():
    fruits = {}
    while True:
        try:
            fruit = input().lower()
            if fruit in fruits:
                fruits[fruit] = fruits[fruit] + 1
            else:
                fruits[fruit] = 1
        except EOFError:
            break
    fruits = dict(sorted(fruits.items()))
    for fruit in fruits:
        print(f"{str(fruits[fruit])} {fruit.upper()}", end="\n")

main()