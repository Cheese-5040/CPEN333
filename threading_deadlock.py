import threading
def worker1(lock1, lock2):
    lock1.acquire()
    print("DEBUG: lock1 acquired, lock2 is next")
    lock2.acquire()
    print("In critical section")
    lock2.release()
    lock1.release()

def worker2(lock1, lock2):
    lock2.acquire()
    print("DEBUG: lock2 acquired, lock1 is next")
    lock1.acquire()
    print("In critical section")
    lock1.release()
    lock2.release()

if __name__ == "__main__":
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    #unlikely that deadlock is going to happen 
    t1=threading.Thread(target=worker1, args=(mutex1, mutex2))
    t1.start()
    t2=threading.Thread(target=worker2, args=(mutex1, mutex2))
    t2.start()
    t1.join()
    t2.join()
