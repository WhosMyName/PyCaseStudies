import time
import multiprocessing

THREADS = multiprocessing.Value("i", 0)
LIMIT = 5

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

                

main()