from datetime import datetime

DATE_FORMAT = "%d/%m/%Y %H:%M:%S %Z%z"


def format_date_time(date_time: datetime) -> str:
    return date_time.strftime(DATE_FORMAT)


def get_current_datetime() -> str:
    return format_date_time(datetime.now())


def parse_datetime_as_object(datetime_as_str: str) -> datetime:
    return datetime.strptime(datetime_as_str, DATE_FORMAT)


def compare_datetime_to_current(date_time_obj: datetime):
    return date_time_obj > datetime.now()
