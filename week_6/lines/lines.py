import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few comand-line arguments!")
    elif len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments!")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    else:
        file_name = sys.argv[1]
        count_lines(file_name)


def count_lines(s):
    try:
        with open(s, "r") as file:
            count = 0
            for line in file:
                line = line.lstrip()
                count += 1
                if line.startswith('#'):
                    count -= 1
                elif line == "":
                    count -= 1
            print(count)
    except FileNotFoundError:
        sys.exit("Python file do not existe!")

if __name__ == "__main__":
    main()