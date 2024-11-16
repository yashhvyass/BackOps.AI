from datetime import datetime, timedelta, timezone

TIMESTAMP_STR = "%m/%d/%Y %H:%M:%S"

def get_current_time_in_str(format=TIMESTAMP_STR):
    return datetime.now().strftime(format)

def get_today_date_attr():
    datetime_obj = datetime.now()
    return datetime_obj.year, datetime_obj.month, datetime_obj.day

def today_stats():
    year, month, day = get_today_date_attr()

    return get_stats(year, month, day)

def get_stats(year: int, month: int, day: int):
    stats = {
        'Inserted': 0,
        'Updated': 0,
        'Deleted': 0
    }
    with open('myapp.log') as f:
        for log in f:
            log = log.strip()

            # Extract year (0 - 3)
            logYear = int(log[0: 4])

            # Extract month (5 - 6)
            logMonth = int(log[5: 7])

            # Extract day (8 - 10)
            logDay = int(log[8: 11])

            # Message of the log
            splitStrList = log.split("-")[-1].lstrip()

            op = splitStrList.split(" ")[0]

            # Process log if it only matches given query criteria
            if year == logYear and month == logMonth and day == logDay:
                stats[op] += 1

    return stats