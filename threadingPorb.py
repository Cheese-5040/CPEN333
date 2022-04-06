import threading, time
class SharedData:
    def __init__(self): 
        self._data : int = 0
    #method 1
    # def increment(self):
    #     lock.acquire() #lock the critical section and let  others wait
    #     x = self.__data
    #     x +=1
    #     time.sleep(0.2)
    #     self.__data= x
    #     lock.release() #release the lock 
    
    #method 2
    def increment(self):
        with lock:
            x = self._data
            x +=1
            time.sleep(0.2)
            self._data= x

    def getdata(self) -> str:
        return self._data


if __name__ == "__main__":
    y = SharedData()
    lock = threading.Lock() #instantiate a lock object
    t1 = threading.Thread(target=y.increment)
    t2 = threading.Thread(target=y.increment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"The shared data's final value: {y._data}")