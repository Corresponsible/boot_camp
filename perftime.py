import  time

def execution_time(measured_function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        measured_function(*args, **kwargs)
        end = time.perf_counter()
        print(f"Time elapsed: {end-start:0.4f} sec")        
    return wrapper

@execution_time
def count_to_number(number):
    for x in range(number):
        time.sleep(1)
        print(x+1)

count_to_number(10)