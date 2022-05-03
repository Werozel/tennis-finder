import datetime

from flask_babel import format_datetime

from helpers.args import get_cookie

DATETIME_FORMATS = {
    'en': ["EEEE, MMM dd, HH:mm", "EEEE, MMM dd YY, HH:mm"],
    'ru': ["EEEE, dd MMM, HH:mm", "EEEE, dd MMM YY, HH:mm"]
}


def format_date_time(dt) -> str:
    dt_format = DATETIME_FORMATS.get(get_cookie('language', 'ru'))
    if not dt_format:
        return format_datetime(dt, "EEEE, MMM dd, HH:mm").title()
    now = datetime.datetime.now()
    if dt.year == now.year:
        return format_datetime(dt, dt_format[0]).title()
    else:
        return format_datetime(dt, dt_format[1]).title()
