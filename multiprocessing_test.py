import sys
import threading
import multiprocessing
from decorators import timer
import time

def busy_wait(n):
    while n > 0:
        n -= 1
        
def sleep_wait(n):
    time.sleep(n)

@timer
def single_threaded_test(func, n):
    for _ in range(4):
        func(n)
        
@timer
def multi_threaded_test(func, n):
    threads = []
    for _ in range(4):
        thread = threading.Thread(target=func, args=(n,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

@timer
def multi_processing_test(func, n):
    processes = []
    for _ in range(1):
        process = multiprocessing.Process(
            target=func, args=(n,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
        
@timer
def busy_test(n):
    print('Starting busy test')
    single_threaded_test(busy_wait, n)
    multi_threaded_test(busy_wait, n)
    multi_processing_test(busy_wait, n)
    
@timer
def sleep_test(n):
    print('Starting sleep test')
    single_threaded_test(sleep_wait, n)
    multi_threaded_test(sleep_wait, n)
    multi_processing_test(sleep_wait, n)
        
if __name__ == '__main__':
    n = 1000000
    busy_test(n)
    print('')
    n = 1
    sleep_test(n)
    
    