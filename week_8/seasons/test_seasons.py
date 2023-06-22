import seasons
import datetime

def main():
    test_lived_time()


def test_lived_time():
    assert seasons.lived_time(datetime.datetime(2022, 12, 31), datetime.datetime(2022, 1, 1)) == datetime.timedelta(days=364)

def test_duration_minutes():
    assert seasons.duration_minutes(datetime.timedelta(days=1)) == 1440

def test_convert_in_words():
    assert seasons.convert_in_words(22) == "Twenty-two minutes"

if __name__ == "__main__":
    main()