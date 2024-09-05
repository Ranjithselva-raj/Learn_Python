### MultiThreading with ThreadPoolExecutor
# with ThreadPoolExecutor we managing the entire threads and this is advance techniques specifically 
# --> used  while we implementing application with mulithreading itself

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):   
        time.sleep(1)
        return f"Number:{number}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)
end = time.time()
print(f"Finished in : {end - start} seconds")