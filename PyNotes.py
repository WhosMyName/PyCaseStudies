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

#--------------------------------------------------------

timer(5)
