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

def new_mabi_time(time):
    ''' input: datetime object, output: time in Mabinogi '''
    secs=((time.hour * 3600) + (time.minute * 60) + time.second) * 40
    zerotime=datetime.datetime.strptime("0:0:0", "%H:%M:%S")
    mabitime=(zerotime+relativedelta(seconds=secs)).time()
    print(f"Time in Mabinogi: {mabitime}")

if __name__=="__main__":
    HELP_TEXT="time in %H:%M:%S format, defaults to current"

    parser=argparse.ArgumentParser(description="Convert time to Mabinogi time")
    parser.add_argument("time", help=HELP_TEXT, nargs='?', type=valid_time, default="")
    args=parser.parse_args()

    new_mabi_time(args.time)
