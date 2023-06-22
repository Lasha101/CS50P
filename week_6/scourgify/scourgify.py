import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few comand-line arguments!")
    elif len(sys.argv) > 3:
        sys.exit("Too many comand-line arguments!")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a python file")
    else:
        before = sys.argv[1]
        after = sys.argv[2]
        convert_file(before, after)

def convert_file(x, y):
    try:
        with open(x, "r") as input_file:
            reader = csv.DictReader(input_file)
            with open(y, "w", newline="" ) as output_file:
                writer = csv.DictWriter(output_file, fieldnames= ["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    l_name, f_name = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": f_name, "last": l_name, "house": house})
    except (FileNotFoundError, PermissionError, ValueError, UnicodeDecodeError, csv.Error) as e:
            sys.exit(f"Could not read {x} {e}")

if __name__ == "__main__":
    main()