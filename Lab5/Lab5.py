#student name: Ow Yong Chee Seng    
#student number: 61164992

import threading
import random #is used to cause some randomness 
import time   #is used to cause some delay in item production/consumption

class circularBuffer: 
    """ 
        This class implement a barebone circular buffer.
        Use as is.
    """
    def __init__ (self, size: int):
        """ 
            The size of the buffer is set by the initializer 
            and remains fixed.
        """
        self._buffer = [0] * size   #initilize a list of length size
                                    #all zeroed (initial value doesn't matter)
        self._in_index = 0   #the in reference point
        self._out_index = 0  #the out reference point

    def insert(self, item: int):
        """ 
            Inserts the item in the buffer.
            The safeguard to make sure the item can be inserted
            is done externally.
        """
        self._buffer[self._in_index] = item #put the item in the in_index
        self._in_index = (self._in_index + 1) % SIZE #increment the in_index once the item is placed

    def remove(self) -> int:
        """ 
            Removes an item from the buffer and returns it.
            The safeguard to make sure an item can be removed
            is done externally.
        """
        item = self._buffer[self._out_index] #select an item from buffer of out_index
        self._out_index = (self._out_index + 1) % SIZE #increment the out_index after removing the item
        return item

def producer() -> None:
    """
        Implement the producer function to be used by the producer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeProduced() -> int: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        return random.randint(1, 99)  #an item is produced

    for _ in range(SIZE * 2): #we just produce twice the buffer size for testing
        item = waitForItemToBeProduced()  #wait for an item to be produced
        print(f"DEBUG: {item} produced")
        #complete the function below here to correctly store the item in the circular buffer
        empty.acquire()     #reduce empty buffers by 1 if buffer is not full, put item in buffer if not full
        mutex.acquire()     #Lock the process since it is in critical region 
        buffer.insert(item) #insert item into buffer
        full.release()      #increase full buffers by 1
        mutex.release()     #release the lock 

def consumer() -> None:
    """
        Implement the consumer function to be used by the consumer thread.
        It must correctly use full, empty and mutex.
    """
    for _ in range(SIZE * 2): #we just consume twice the buffer size for testing
        #write the code below to correctly remove an item from the circular buffer
        full.acquire()          #reduce the number of full buffers by 1, put item in buffer if not empy 
        mutex.acquire()         #lock the process since it is in critical region 
        item = buffer.remove()  #remove item from buffer
        empty.release()         #increase empty buffers by 1
        mutex.release()         #release the lock
        #end of your implementation for this function
        #use the following code as is
        def waitForItemToBeConsumed(item) -> None: #inner function; use as is
            time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
            #to simulate consumption, item is thrown away here by just ignoring it
        waitForItemToBeConsumed(item)  #wait for the item to be consumed
        print(f"DEBUG: {item} consumed")

if __name__ == "__main__":
    SIZE = 5  #buffer size
    buffer = circularBuffer(SIZE)  #initialize the buffer

    full = threading.Semaphore(0)         #full semaphore: number of full buffers
                                          #initial value set to 0
    empty = threading.Semaphore(SIZE)     #empty semaphore: number of empty buffers
                                          #initial value set to SIZE
                                          #5 treads can print concurrently 
    mutex = threading.Lock()  #lock for protecting data on insertion or removal

    #complete the producer-consumer thread creation below
    # print(f"full buffer {full._value}")
    # print(f"empty buffer {empty._value}")
    produce = threading.Thread(target=producer) #create a thread for the producer
    consume = threading.Thread(target=consumer) #create a thread for the consumer
    produce.start() #start the producer thread
    consume.start() #start the consumer thread
    produce.join()  #join the thread
    consume.join()  #join the thread