import threading
import concurrent.futures
import time

start = time.time()

def do_something():
    print('Sleeping for 1 sec. ...')
    time.sleep(1)
    print('Done Sleeping ...')
#-----------------------
# do_something()
# do_something()
# =======================

# -----------------------------------------------
# t1 = threading.Thread(target= do_something )
# t2 = threading.Thread(target= do_something )
# #  start Threading
# t1.start()
# t2.start()
#
# # join Threading
#
# t1.join()
# t2.join()
# =================================================

# using ThreadPoolExecutor



finish = time.time()

print(f'Fiinished in {round(finish-start , 3)} sec.')