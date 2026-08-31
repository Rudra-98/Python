import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


@timer
def slow_add(a, b, delay=0.5):
    time.sleep(delay)
    return a + b

result = slow_add(3, 4, delay=1)
print(result)  # 7
print(slow_add.__name__)  # slow_add (not "wrapper")