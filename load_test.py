#!/usr/bin/env python

from threading import Event, Thread,current_thread
from urllib.parse import urlencode
import httplib2, random, socket, time

# Modify these values to control how the testing is done

# How many threads should be running at peak load.
NUM_THREADS = 10

# How many minutes the test should run with all threads active.
TIME_AT_PEAK_QPS = 10 # minutes

# How many seconds to wait between starting threads.
# Shouldn't be set below 30 seconds.
DELAY_BETWEEN_THREAD_START = 30 # seconds

quitevent = Event()

def threadproc():
    """This function is executed by each thread."""
    print ("Thread started: %s" % current_thread().getName())
    h, i = httplib2.Http(timeout=30), 0
    while not quitevent.is_set():
        try:
            # HTTP requests to exercise the server go here
            resp, content = h.request("https://beta.tokopedia.com/tokoqc14/")
            if resp.status != 200:
                print("Response code", resp.status)
        except socket.timeout:
            pass

    print ("Thread finished: %s" % current_thread().getName())


if __name__ == "__main__":
    runtime = (TIME_AT_PEAK_QPS * 60 + DELAY_BETWEEN_THREAD_START * NUM_THREADS)
    print ("Total runtime will be: %d seconds" % runtime)
    threads = []
    try:
        for i in range(NUM_THREADS):
            t = Thread(target=threadproc)
            t.start()
            threads.append(t)
            time.sleep(DELAY_BETWEEN_THREAD_START)
        print ("All threads running")
        time.sleep(TIME_AT_PEAK_QPS*60)
        print ("Completed full time at peak qps, shutting down threads")
    except:
        print ("Exception raised, shutting down threads")

    quitevent.set()
    time.sleep(3)
    for t in threads:
        t.join(1.0)
    print ("Finished")