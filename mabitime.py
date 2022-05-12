import sys
import datetime
import argparse
from dateutil.relativedelta import relativedelta

def valid_time(time):
    if time is None or time=="":
        return datetime.datetime.now()
    try:
        return datetime.datetime.strptime(time, "%H:%M:%S")
    except ValueError:
       msg=f"{time} is not a valid time"
       raise argparse.ArgumentTypeError(msg)

def old_mabi_time(time):
    totl, mabi, mabihour, mabimins = 0, 0, 0, 0
    hour = time.hour
    mins = time.minute
    secs = time.second
    totl = (hour * 60) + mins
    mabi = totl * 40 - 40
    mabihour = mabi // 60
    mabimins = mabi % 60
    mabihour = mabihour % 24
    if mabimins < 0:
        mabihour -= 1
        mabimins += 60
    if mabihour < 0:
        mabihour += 12
    print(f"Time in Mabinogi: {mabihour}:{mabimins}")

def new_mabi_time(time):
    print(f"Time entered: {time}")
    secs=((time.hour * 3600) + (time.minute * 60) + time.second) * 40 - 2400
    #timeshift=datetime.timedelta(seconds=secs)
    zerotime=datetime.datetime.strptime("0:0:0", "%H:%M:%S")
    mabitime=(zerotime+relativedelta(seconds=secs)).time()
    print(f"Time in Mabinogi: {mabitime.strftime('%H:%M:%S')}")
    #print(f"Time in Mabinogi: {time + timeshift}")

if __name__=="__main__":
    help_text="time in %H:%M:%S format, defaults to current"

    parser=argparse.ArgumentParser(description="Convert time to Mabinogi time")
    parser.add_argument("time", help=help_text, nargs='?', type=valid_time, default="")
    args=parser.parse_args()

    print("Old method (pretty accurate)")
    old_mabi_time(args.time)
    print("New method (not there yet)")
    new_mabi_time(args.time)
