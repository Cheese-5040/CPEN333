import threading, time

def worker(greetings):
    for _ in range(3):
        print("Say ", end="")
        time.sleep(0.2)
        print(greetings)

if __name__ == "__main__":
    threading.Thread(target=worker, args=("aloha",)).start()
    threading.Thread(target=worker, args=("ciao",)).start()