import functools

def retry(times=3, exceptions=(ValueError,)):
    def decorator(func):
        @functools.wraps(func)          # preserves func's __name__, __doc__, etc.
        def wrapper(*args, **kwargs):   # accept any args so it works on any function
            last_exception = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)   # success -> return immediately, no wasted retries
                except exceptions as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise last_exception            # re-raise the ACTUAL exception after all attempts fail
        return wrapper
    return decorator


@retry(times=3, exceptions=(ValueError,))
def say_hello():
    print("hi nikitha-chandu")

say_hello()
#################################################################################################################

attempt_count = 0

@retry(times=3, exceptions=(ValueError,))
def flaky():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ValueError(f"failed on attempt {attempt_count}")
    return "success!"

print(flaky())
# Attempt 1 failed: failed on attempt 1
# Attempt 2 failed: failed on attempt 2
# success!
