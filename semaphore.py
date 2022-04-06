import threading, time 
def worker(printers):
    with printers:
        print(f"thread {threading.current_thread().name}can print")
        time.sleep(1.5)

if __name__ == "__main__": 
    printers = threading.Semaphore(3) #three threads can print concurrently 
    for i in range (20): 
        threading.Thread(target=worker, args = (printers, )).start()