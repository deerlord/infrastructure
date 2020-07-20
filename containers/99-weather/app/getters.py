import datetime
import pytz


def _convert_utc_to_cst(timestamp):
    dtime = datetime.datetime.fromtimestamp(timestamp)
    return dtime.replace(
        tzinfo=datetime.timezone.utc
    ).astimezone(tz=pytz.timezone('America/Chicago'))
