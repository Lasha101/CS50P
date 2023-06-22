def main():
    enter_date()

def enter_date():
    while True:
        date = input("Date:")
        date = date.strip()
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        try:
            month, day, year = date.split("/")
            month = int(month)
            if ((month > 0 and  month <=12) and (int(day) > 0 and int(day) <=31) and len(year) == 4):
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
        except ValueError:
            try:
                month_day, year = date.split(",")
                year = year.strip()
                month, day = month_day.split(None, 1)
                month = month.capitalize()
                if (month in month_list) and (int(day) > 0 and int(day) <=31) and len(year) == 4:
                    month_num = month_list.index(month) + 1
                    print(f"{year}-{month_num:02}-{int(day):02}")
                    break
            except ValueError:
                continue

main()
