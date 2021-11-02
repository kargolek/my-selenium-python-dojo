from datetime import datetime

import pytz

DATE_FORMAT = "%d/%m/%Y %H:%M:%S %Z%z"


def set_datetime_to_utc(date_time: datetime) -> datetime:
    return date_time.astimezone(pytz.utc)


def compare_datetime_to_current(date_time_obj: datetime):
    return date_time_obj > datetime.now().astimezone(pytz.utc)
