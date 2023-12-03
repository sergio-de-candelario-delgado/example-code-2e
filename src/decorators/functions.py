from decorators.decorators import change_text_uppercase, change_text_lowercase, change_text_upper_or_lower


def say_hello(name: str) -> str:
    return f"Hello {name}"


@change_text_uppercase
def say_hello_in_uppercase_with_decorators(name: str) -> str:
    return say_hello(name)


@change_text_lowercase
def say_hello_in_lowercase_with_decorators(name: str) -> str:
    return say_hello(name)


@change_text_upper_or_lower("upper")
def say_hello_in_uppercase_with_parametrized_decorator(name: str) -> str:
    return say_hello(name)


@change_text_upper_or_lower("lower")
def say_hello_in_lowercase_with_parametrized_decorator(name: str) -> str:
    return say_hello(name)


@change_text_upper_or_lower("invalid")
def say_hello_in_invalid_type_with_parametrized_decorator(name: str) -> str:
    return say_hello(name)

