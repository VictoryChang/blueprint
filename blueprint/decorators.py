import functools
import sys
import time


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


def repeat(iterations: int = 3):
    """
    Repeat the decorated function

    :param iterations: Number of iterations
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(iterations):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def validate_status(code: int):
    """
    Validate the status code of the decorated function result.
    Assumes result has attribute status_code.

    :param code: Expected status code
    """
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


def retry(iterations: int = 3):
    """
    Retry the decorated function for n iterations until non-exception occurs

    :param iterations: Number of iterations
    """
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
