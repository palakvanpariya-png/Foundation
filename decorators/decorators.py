import functools
import time

def say_twice(func):
    @functools.wraps(func)
    def wrapper_say_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_say_twice

def calculate_time(func):
    @functools.wraps(func)
    def wrapper_calculate_time(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper_calculate_time