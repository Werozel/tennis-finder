import datetime

from tennis_finder.helpers.datetime_helper import format_date_time

from tennis_finder.modules.core.app_config import AppConfig


def test_format_datetime(mocker):
    mocker.patch("tennis_finder.helpers.args.get_cookie", new=lambda k, d: d)
    with AppConfig.app.app_context():
        dt_formatted = format_date_time(datetime.datetime.now())
        mocker.patch("tennis_finder.helpers.args.get_cookie", new=lambda k, d: 'en')
        dt_formatted_2 = format_date_time(datetime.datetime.now())

        assert dt_formatted != dt_formatted_2
