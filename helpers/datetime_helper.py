"""This module contains datetime helpers."""
import datetime

from flask_babel import format_datetime

import helpers.args

DATETIME_FORMATS = {
    'en': ["EEEE, MMM dd, HH:mm", "EEEE, MMM dd YY, HH:mm"],
    'ru': ["EEEE, dd MMM, HH:mm", "EEEE, dd MMM YY, HH:mm"]
}


def format_date_time(dt: datetime.datetime) -> str:
    """
    Format datetime depending on language.

    :param dt: datetime object to format
    :return: formatted datetime string
    """
    dt_format = DATETIME_FORMATS.get(helpers.args.get_cookie('language', 'ru'))
    if not dt_format:
        return format_datetime(dt, "EEEE, MMM dd, HH:mm").title()
    now = datetime.datetime.now()
    if dt.year == now.year:
        return format_datetime(dt, dt_format[0]).title()
    else:
        return format_datetime(dt, dt_format[1]).title()
