def main():
    time = input("What time is it? ")
    z = convert(time)
    if z >= 7.0 and z <= 8.0:
        print("breakfast time")
    elif z >= 12.0 and z <= 13.0:
        print("lunch time")
    elif z >= 18.0 and z <= 19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    x = float(minutes) / 60
    y = float(hours)
    t = y + x
    return float(t)

if __name__ == "__main__":
    main()

