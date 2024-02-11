import pytest

from typing import Callable

from decorators.decorators import change_text_uppercase, change_text_lowercase
from decorators.functions import say_hello, say_hello_in_uppercase_with_decorators, \
    say_hello_in_lowercase_with_decorators, say_hello_in_uppercase_with_parametrized_decorator, \
    say_hello_in_lowercase_with_parametrized_decorator, say_hello_in_invalid_type_with_parametrized_decorator


class TestDecoratorsAsFunctions:

    @pytest.mark.parametrize(
        "function, expected",
        [
            (change_text_uppercase, "HELLO SERGIO"),
            (change_text_lowercase, "hello sergio"),
        ]
    )
    def test_case_conversions_without_decorators(self, function: Callable, expected: str):
        assert function(say_hello)("Sergio") == expected

    @pytest.mark.parametrize(
        "function, expected",
        [
            (say_hello_in_uppercase_with_decorators, "HELLO SERGIO"),
            (say_hello_in_lowercase_with_decorators, "hello sergio"),
            (say_hello_in_uppercase_with_parametrized_decorator, "HELLO SERGIO"),
            (say_hello_in_lowercase_with_parametrized_decorator, "hello sergio"),
        ]
    )
    def test_case_conversions_with_decorators(self, function: Callable, expected: str):
        assert function("Sergio") == expected

    def test_not_change_text_with_invalid_argument_parametrized_decorator(self):
        with pytest.raises(Exception, match="Not valid type invalid"):
            say_hello_in_invalid_type_with_parametrized_decorator("Sergio")
