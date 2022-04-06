from multiprocessing import shared_memory, Process
import numpy as np
def process2(dataSize, dataType):
    existing_shm = shared_memory.SharedMemory(name="demoSM") #attach to existing shared memory block , name is demoSM
    b = np.ndarray((dataSize,), dtype=dataType, buffer=existing_shm.buf) #create an array, buffer is used to fill the array with data
    print(f"Child process has access to {b}")
    existing_shm.close() #clean up from within the child process

if __name__ == "__main__":
    a = np.array([1, 1, 2, 3, 5, 8])
    shm = shared_memory.SharedMemory(name="demoSM", create=True, size=a.nbytes) #unique name, and fix size 
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf) #create an array of process b
    b[:]=a[:]
    p = Process(target=process2, kwargs={"dataSize": a.size, "dataType": type(a[0])})
    p.start()
    p.join()
    shm.close() #clean up from within the main process
    shm.unlink() #free and release the shared memory block at the very end
    