def main():
    in_list_input_names()
    print_constructed_string()

import inflect
p = inflect.engine()

input_names = []

def in_list_input_names():
    while True:
        try:
            entered_name = input("Name:")
        except EOFError:
            break
        else:
            input_names.append(entered_name)

def print_constructed_string():
    print("Adieu, adieu, to", p.join(input_names))

main()