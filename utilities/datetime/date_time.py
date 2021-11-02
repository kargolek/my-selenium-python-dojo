from datetime import datetime

import pytz

DATE_FORMAT = "%d/%m/%Y %H:%M:%S %Z%z"


def set_datetime_to_utc(date_time: datetime) -> datetime:
    return date_time.astimezone(pytz.utc)


def format_date_time_tz_utc(date_time: datetime) -> str:
    return date_time.strftime(DATE_FORMAT)


def parse_datetime_as_object(datetime_as_str: str) -> datetime:
    return datetime.strptime(datetime_as_str, DATE_FORMAT)


def compare_datetime_to_current(date_time_obj: datetime):
    return date_time_obj > datetime.utcnow()
