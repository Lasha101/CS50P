import sys
from datetime import datetime
from datetime import date
import inflect
p = inflect.engine()

def main():
   convert_in_words(duration_minutes(lived_time(current_time(), birth_date())))

def birth_date():
    try:
        user_input = input("Enter your date of birth (YYYY-MM-DD): ")
        date = datetime.strptime(user_input, "%Y-%m-%d").date()
        return date
    except ValueError as e:
        sys.exit(f"Invalid date: {e}")

def current_time():
    return date.today()

def lived_time(current_time, birth_date):
    return current_time - birth_date

def duration_minutes(lived_time):
    lived_days = lived_time.days
    return lived_days * 24 * 60

def convert_in_words(duration):
    print(p.number_to_words(duration, andword="").capitalize() + " minutes")
    return f"{p.number_to_words(duration, andword='').capitalize()} minutes"
if __name__ == "__main__":
    main()