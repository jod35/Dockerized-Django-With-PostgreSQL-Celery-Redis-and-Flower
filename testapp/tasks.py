import time
from datetime import datetime
from celery import shared_task

@shared_task
def long_running_task(delay):
    start_time = datetime.now()
    print("##### started task at {}".format(start_time))

    time.sleep(int(delay))
    end_time = datetime.now()
    print("##### ended task at {}".format(end_time))
    
    time_diff = end_time - start_time
    print("Finished task at {}s".format(time_diff))
    print("#########################################################")

    return f"{time_diff}s"