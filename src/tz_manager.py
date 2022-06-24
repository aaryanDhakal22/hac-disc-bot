import pytz
from pytz import UnknownTimeZoneError
from datetime import datetime


def is_timezone(tz):
    try:
        tz_check = pytz.timezone(tz)
    except UnknownTimeZoneError:
        tz_check = None
    if tz_check != None:
        return tz_check
    else:
        return False


def dt_formatter(dt):
    return dt.strftime("%I:%M %p, %B %d")


def time_for_zone(tz_list):
    result = {}
    for timezone in tz_list:
        tz = pytz.timezone(timezone)
        formatted = dt_formatter(datetime.now(tz))
        result.setdefault(timezone, formatted)
    return result


def return_tzs_for_stored():
    tz_file = open("../assets/timezone_list.txt", "r")
    tz_content = tz_file.readlines()
    tzs = [item.strip() for item in tz_content]
    tz_file.close()
    return time_for_zone(tzs)
