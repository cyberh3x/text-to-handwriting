import calendar
import time


def getCurrentTimestamp():
    gmt = time.gmtime()
    timestamp = calendar.timegm(gmt)
    return timestamp
