## MultiProcessing 
# Process that run in parellel
# when to use multiprocessing
# 1.CPU bound tasks: Tasks that spend most of their time on CPU operations like ( Data processing, Mathematical operations, etc)
# 2.Parellel execution : Multiple cores of CPU can be used to execute multiple tasks at the same time

import time
import multiprocessing

def Square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i**2}")

def Cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube:{i**3}")




if __name__ == "__main__":
    ## Create  2 processes
    p1 = multiprocessing.Process(target=Square_numbers)
    p2 = multiprocessing.Process(target=Cube_numbers)

    start = time.time()
    # Start both processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    end = time.time()
    print(f"Finished in : {end - start} seconds")