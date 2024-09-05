## Multithreading
# when to use multithreading
# I/O bound tasks: Tasks that spend more time on I/O operations like (reading files, writing files, network requests, etc)
# Concurrent execution: When you want to improve the throughput of your application by performing multiple tasks concurrently

import time
import threading

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letters():
    for i in "abcde":
        time.sleep(1)
        print(f"Letter:{i}")
    

## Create  2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

start = time.time()
# Start both threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

end = time.time()
print(f"Finished in : {end - start} seconds")

#without multithreading Finished in : 15.056011199951172 seconds 
# with multithreading Finished in : 10.000000953674316 seconds