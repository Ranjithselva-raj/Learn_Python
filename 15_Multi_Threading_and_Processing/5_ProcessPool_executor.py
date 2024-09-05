## MultiProcessing with ProcessPoolExecutor
# with ProcessPoolExecutor we managing the entire processes and this is advance techniques specifically

from concurrent.futures import ProcessPoolExecutor
import time

def sqaure_numbers(number):
    time.sleep(2)
    return f"Square:{number**2}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

if __name__ == "__main__":

    start = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(sqaure_numbers, numbers)

    for result in results:
        print(result)
    end = time.time()
    print(f"Finished in : {end - start} seconds")

#with 3 workers Finished in : 14.131766319274902 seconds
#with 6 workers Finished in : 8.12151288986206 seconds
#with 10 workers Finished in : 4.197086334228516 seconds