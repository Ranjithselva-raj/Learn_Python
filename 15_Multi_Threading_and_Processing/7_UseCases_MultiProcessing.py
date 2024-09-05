"""
Real World example: MultiProcessing for CPU bound tasks
Scenario : Factorial Calculation
Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance.

"""

import time
import math
import multiprocessing
import sys

#increase the maximum number of digits for integer conversion

sys.set_int_max_str_digits(100000)
#function to compute factorial of a given number
def factorial_number(number):
    print(f'Factorial of {number}')
    time.sleep(1)
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == "__main__":
    numbers = [4000,4001,4500,5000,6000,7000,8000,9000,10000]
    start = time.time()
    #create a pool of worker process
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial_number, numbers)
    end = time.time()
    print(results)
    print(f"Finished in : {end - start} seconds")

#Finished in : 1.6340065002441406 seconds