import multiprocessing
def worker():
    try:
        print(f"Trying to access var: {var}")
    except NameError:
        print("Nope, doesn't have access")
if __name__ == "__main__":
    var = "hello"
    multiprocessing.Process(target=worker).start()
