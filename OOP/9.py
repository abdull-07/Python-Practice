# Create your own decorator that logs function name & execution time

import time
def my_decorator(func):
    def wrapper():
        print(f"Executing {func.__name__}")
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time}")
    return wrapper

@my_decorator
def gether():
    for i in range(1000000):
        print(i)

gether()