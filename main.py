import socket
import struct
import sys
import time
from datetime import datetime
import ntplib
from tqdm import tqdm

ntp_server = 'time.google.com'

def get_ntp_timestamp():
    call = ntplib.NTPClient()
    response = call.request(ntp_server, version=3)
    t = datetime.fromtimestamp(response.orig_time)
    return t

def GetTimeInVariables():
    timestamp = get_ntp_timestamp()

    "timestamp.strftime('%a %b %d %H:%M:%S.%f')"

    digitalclock = timestamp.strftime("%H:%M:%S")
    'hours = timestamp.strftime("%H")'
    'minutes = timestamp.strftime("%M")'
    'seconds = timestamp.strftime("%S")'
    milliseconds = int(timestamp.strftime("%f"))/1000

    return {'digitalclock': digitalclock, 'milliseconds': milliseconds}

def start():
    currentTime = GetTimeInVariables();
    currentMS = currentTime['milliseconds']

if __name__ == "__main__":
    with tqdm(total=100) as pbar:  
        while True:
            currentTime = GetTimeInVariables();
            currentMS = int(currentTime['milliseconds'])            

            cur_perc = currentMS/10
            pbar.update(cur_perc - pbar.n)  # here we update the bar of increase of cur_perc
            pbar.set_description(currentTime['digitalclock'])

            if cur_perc == 100:
                break

    



 
