import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few comand-line arguments!")
    elif len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments!")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a python file")
    else:
        file_name = sys.argv[1]
        print_menu(file_name)

def print_manu(s):
    try:
        with open(s, newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = [row for row in reader]
        print(tabulate(data, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("Python file do not existe!")

if __name__ == "__main__":
    main()