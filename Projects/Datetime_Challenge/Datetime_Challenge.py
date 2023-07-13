
from datetime import datetime
import pytz



datetime_Honolulu = datetime.now(pytz.timezone('Pacific/Honolulu'))
print("The time in Hawaii is: ", datetime_Honolulu.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

datetime_Portland = datetime.now(pytz.timezone('US/Pacific'))
if datetime_Portland == 9 > datetime_Portland.strftime('%H') > 17:
    print("The Portland office is OPEN at ",datetime_Portland.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
else:
    print("The Portland office is CLOSED at ",datetime_Portland.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

datetime_NewYork = datetime.now(pytz.timezone('America/New_York'))
if datetime_NewYork == 9 > datetime_NewYork.strftime('%H') > 17:
    print("The New York office is OPEN at ",datetime_NewYork.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
else:
    print("The New York office is CLOSED at ",datetime_NewYork.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

datetime_London = datetime.now(pytz.timezone('Europe/London'))
if datetime_London == 9 > datetime_London.strftime('%H') > 17:
    print("The London office is OPEN at ",datetime_London.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
else:
    print("The London office is CLOSED at ",datetime_London.strftime('%Y:%m:%d %H:%M:%S %Z %z'))










"""
from datetime import *


today = date.today()
now = datetime.now()

print(today)

dt_string = now.strftime("%B%d%Y %Z")
dt_string = now.strftime("%B%d%Y %Z")

print("The time right now in Hawaii is: " + now + "at " + dt_string)
"""
