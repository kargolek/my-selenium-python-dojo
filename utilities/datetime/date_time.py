from datetime import datetime

import pytz


def get_naive_utc_current_dt():
    return datetime.now().astimezone(pytz.utc)


def is_earlier_date(date_time_obj: datetime, now_date: datetime):
    return date_time_obj > now_date
