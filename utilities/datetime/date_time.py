from datetime import datetime

import pytz

# DATE_FORMAT = "%d/%m/%Y %H:%M:%S %Z%z"


def set_datetime_to_utc(date_time: datetime) -> datetime:
    return date_time.astimezone(pytz.utc)


def get_naive_utc_current_dt():
    return datetime.now().astimezone(pytz.utc)


def is_earlier_date(date_time_obj: datetime, now_date: datetime):
    return date_time_obj > now_date
