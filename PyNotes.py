#Extremely Important
if os.name == "nt":
    SLASH = "\\"
else:
    SLASH = "/"

#To do anything based on OS put this in a Function



#How to create a Timer based on current Time

import sys
from datetime import *
#---Cycling Timer (Stuffz after Time) Use sleep(secs) u secsstoopid cunt
def timer(Time):
    dt = datetime.now()    #Var for less writing, place this based on event or handler
    seconds = dt.second    #Current second saved in Var
    reached = True
    print(str(dt.second))
    if seconds + Time >= 60:
        seconds = seconds - 60
    while reached:    #Comparison
        dt = datetime.now()
        if dt.second == seconds + Time:
            reached = False
            print(str(dt.second))
            #do_stuff()
            seconds = dt.second    #Incrementation
    exit(0)

#---Periodic Timer (Stuffz over Time)
def overtimer(Time):
    dt = datetime.now()    #Var for less writing, place this based on event or handler
    seconds = dt.second    #Current second saved in Var
    x = 0
    while x < Time:
        dt = datetime.now()
        if dt.second == seconds + 1:    #Comparison
            seconds = dt.second
            x = x + 1
            print(str(dt.second))
            #do_stuff()

#---Download Files via Requests (install via pip)
import requests

def download(url, outname):
    header = requests.utils.default_headers()
    header.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",})

    with open(outname, "wb") as file:#open in binary write mode
        response = requests.get(url, headers=header)#get request
        file.write(response.content)#write to file
    return
#GG