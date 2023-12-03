import functools
from typing import Callable


def change_text_uppercase(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def change_text_lowercase(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()

    return wrapper


def change_text_upper_or_lower(case_type: str) -> Callable:
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)

            if case_type == "lower":
                return value.lower()
            elif case_type == "upper":
                return value.upper()
            else:
                raise Exception(f"Not valid type {case_type}")

        return wrapper

    return decorator
