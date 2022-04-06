import multiprocessing
import time, random

def worker1(lock1, lock2):
    lock1.acquire()
    print(f"DEBUG {multiprocessing.current_process().name}: lock1 acquired, waiting for lock2")
    #worker 1 wait from 0-1s randomly 
    time.sleep(random.random()) #increasing deadlock possibility (0 to 1 sec wait randomly)
    lock2.acquire()
    print("In critical section")
    lock2.release()
    lock1.release()

def worker2(lock1, lock2):
    lock2.acquire()
    print(f"DEBUG {multiprocessing.current_process().name}: lock2 acquired, waiting for lock1")
    #worker 2 wait from 0-1s ranodmly 
    time.sleep(random.random()) #increasing deadlock possibility (0 to 1 sec wait randomly)
    lock1.acquire()
    print("In critical section")
    lock1.release()
    lock2.release()

if __name__ == "__main__":
    mutex1 = multiprocessing.Lock()
    mutex2 = multiprocessing.Lock()
    '''
    since time is random, both might reach deadlock if worker 1 acquire lock1 and worker 2 acquire lock 2
    but there is a chance where worker 1 acquire lock1 and lock 2 and release both before worker 2 acquire lock 2
    '''
    t1=multiprocessing.Process(target=worker1, args=(mutex1, mutex2))
    t1.start()
    t2=multiprocessing.Process(target=worker2, args=(mutex1, mutex2))
    t2.start()
    t1.join()
    t2.join()
