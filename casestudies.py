import time
import multiprocessing

THREADS = multiprocessing.Value("i", 0)
LIMIT = 5
"""
def deeks(THREADS):
    time.sleep(10)
    THREADS.value = THREADS.value - 1
    print("Closing Process")
    return


def main():
    global THREADS
    for x in range(0, 20):
        print("Threads: " + str(THREADS.value))
        print("Episode: " + str(x))
        twerk = multiprocessing.Process(target=deeks, args=(THREADS, ))
        THREADS.value = THREADS.value + 1
        twerk.start()    
        while THREADS.value == LIMIT:
            time.sleep(1)

"""        
def rikt(x, retval):
    print("Yo, Process Nr.", x, "here")
    THREADS.value = THREADS.value + 1
    print("Retval:", retval.value)
    time.sleep(5)
    print(x*2)
    retval.value = x
    return 0        

PROCLST = []

def main():
    pool = multiprocessing.Pool(processes=4 )

    retlist = []
    for x in range(0, 11):
        retval = multiprocessing.Value("i", -1)
        retlist.append(retval)
        worker = multiprocessing.Process(target=rikt, args=(x, retlist[x]))
        worker.start()
        print("Treads:", THREADS.value)
        while THREADS.value == LIMIT:
            time.sleep(1)
        print("Proc returned with Exitcode", retlist[x].value)

        



main()