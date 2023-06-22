
import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    reg_ex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    matching = re.search(r"^" + reg_ex + " to " + reg_ex + "$", s)
    if matching:
        out_of_time = standardize(matching.group(1), matching.group(2), matching.group(3))
        time_time = standardize(matching.group(4), matching.group(5), matching.group(6))
        return f"{out_of_time} to {time_time}"
    else:
        raise ValueError

def standardize(hr, minimum, t):
    if hr == "12":
        if t == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if t == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if minimum == None:
        minute = "00"
    else:
        minute = f"{int(minimum):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()