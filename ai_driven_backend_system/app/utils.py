from datetime import datetime, timedelta, timezone

TIMESTAMP_STR = "%m/%d/%Y %H:%M:%S"

def get_current_time_in_str(format=TIMESTAMP_STR):
    return datetime.now().strftime(format)