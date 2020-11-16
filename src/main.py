#!/usr/bin/python3.8
import calendar
from send_notification import sendmessage


if __name__ == "__main__":
    sendmessage("Test", "Ceci est un test")
yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))