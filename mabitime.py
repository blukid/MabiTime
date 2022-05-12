''' Mabinogi time converter '''
import datetime
import argparse
from dateutil.relativedelta import relativedelta

def valid_time(time):
    ''' determine if inputted time is valid '''
    if time is None or time=="":
        return datetime.datetime.now()
    try:
        return datetime.datetime.strptime(time, "%H:%M:%S")
    except ValueError:
        msg=f"{time} is not a valid time"
        raise argparse.ArgumentTypeError(msg)

def old_mabi_time(time):
    ''' old method, can delete once new works '''
    totl, mabi, mabihour, mabimins = 0, 0, 0, 0
    hour = time.hour
    mins = time.minute
    secs = time.second
    totl = (hour * 60) + mins
    # the "-40" part is a manual correction from old version, may no longer be correct
    mabi = totl * 40 - 40
    mabihour = mabi // 60
    mabimins = mabi % 60
    mabihour = mabihour % 24
    if mabimins < 0:
        mabihour -= 1
        mabimins += 60
    if mabihour < 0:
        mabihour += 12
    print(f"\tTime in Mabinogi: {mabihour}:{mabimins}")

def new_mabi_time(time):
    ''' new method, check if correction below is accurate '''
    # if manual correction is wrong, remove the "-2400" here too
    secs=((time.hour * 3600) + (time.minute * 60) + time.second) * 40 - 2400
    zerotime=datetime.datetime.strptime("0:0:0", "%H:%M:%S")
    mabitime=(zerotime+relativedelta(seconds=secs)).time()
    print(f"\tTime in Mabinogi: {mabitime}")

if __name__=="__main__":
    ''' main method '''
    HELP_TEXT="time in %H:%M:%S format, defaults to current"

    parser=argparse.ArgumentParser(description="Convert time to Mabinogi time")
    parser.add_argument("time", help=HELP_TEXT, nargs='?', type=valid_time, default="")
    args=parser.parse_args()

    print(f"Entered time: {args.time}")
    print("Old method (pretty accurate)")
    old_mabi_time(args.time)
    print("New method (may be there!)")
    new_mabi_time(args.time)
