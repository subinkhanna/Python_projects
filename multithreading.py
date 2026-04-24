##Multithreading - to perform multiple tasks concurrently - multitasking. Good for I/O bound tasks like reading files 
##or fetching data from APIs.    
## Thread(target=my_function)


import threading
import time

def walk(x):
    time.sleep(10)
    print(f"Take the walk {x} steps")


def brush():
    time.sleep(2)
    print("Finish brushing the teeth")


def pack():
    time.sleep(4)
    print("Pack your bag")


task1 = threading.Thread(target=walk, args=(40,))
task1.start()
task2 = threading.Thread(target=brush)
task2.start()
task3 = threading.Thread(target=pack)
task3.start()

print("program is running")

# .join() ensures that all tasks are completed before proceeding
task1.join()
task2.join()
task3.join()
#####

print("program just finished")