import threading
def worker1(lock1, lock2):
    lock1.acquire() #instead of acquire and release, can use WITH 
    #with is done under the hood, not finally
    print("DEBUG: lock1 acquired, waiting for lock2")
    while not lock2.locked(): pass #ensuring deadlock for demo, wait until lock2 is taken 
    lock2.acquire()
    print("In critical section")
    lock2.release()
    lock1.release()

def worker2(lock1, lock2):
    lock2.acquire()
    print("DEBUG: lock2 acquired, waiting for lock1")
    while not lock1.locked(): pass #ensuring deadlock for demo, wait until lock 1 is acquired
    lock1.acquire()
    print("In critical section")
    lock1.release()
    lock2.release()

if __name__ == "__main__":
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    t1=threading.Thread(target=worker1, args=(mutex1, mutex2))
    t1.start()
    t2=threading.Thread(target=worker2, args=(mutex1, mutex2))
    t2.start()
    t1.join()
    t2.join()