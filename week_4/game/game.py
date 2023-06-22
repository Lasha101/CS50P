from random import randint
import sys

def main():
    guess_input(random_digit(level_input()))

def level_input():
    while True:
        try:
            n = input("Level:")
            n = int(n)
            if n > 0:
                return n
            else:
                continue
        except ValueError:
            continue

def random_digit(n):
    try:
        n > 0
    except ValueError:
        pass
    else:
        x = randint(0, n)
        return x

def guess_input(n):
    while True:
        try:
            guess = input("Guess:")
            guess = int(guess)
            if guess <= 0 :
                continue
            elif guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                sys.exit("Just right!")
        except ValueError:
            continue

main()
