import functools
import sys
import time

import requests


def timer(func):
    """ Print the runtime of the decorated function """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f'Finished {func.__name__!r} in {duration:.4f} seconds')
        return result
    return wrapper


@timer
def play():
    print('playing')
    time.sleep(3)


# play()


def repeat(iterations=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(iterations):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat()
def sleep():
    print('sleeping')
    time.sleep(3)

# sleep()


def validate_status(code):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            actual_code = response.status_code
            if actual_code != code:
                msg = f'Function {func.__name__!r} returned status code: {actual_code}, expected: {code}'
                raise RuntimeError(msg)
            return response
        return wrapper
    return decorator


def retry(iterations=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            count = 0
            while count < iterations:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(sys.exc_info())
                    count += 1
            else:
                msg = f'Function {func.__name__!r} failed to complete after {iterations} iterations'
                raise RuntimeError(msg)
        return wrapper
    return decorator


@retry(iterations=5)
@validate_status(code=201)
def value():
    return requests.get('https://google.com')


response = value()
print(response.status_code)
