import pytest

from decorators.decorators import change_text_uppercase, change_text_lowercase
from decorators.functions import say_hello, say_hello_in_uppercase_with_decorators, \
    say_hello_in_lowercase_with_decorators, say_hello_in_uppercase_with_parametrized_decorator, \
    say_hello_in_lowercase_with_parametrized_decorator, say_hello_in_invalid_type_with_parametrized_decorator


class TestDecoratorsAsFunctions:

    def test_change_text_to_uppercase_without_decorators(self):
        text = change_text_uppercase(say_hello)("Sergio")

        assert "HELLO SERGIO" == text

    def test_change_text_to_lowercase_without_decorators(self):
        text = change_text_lowercase(say_hello)("Sergio")

        assert "hello sergio" == text

    def test_change_text_to_uppercase_with_decorators(self):
        text = say_hello_in_uppercase_with_decorators("Sergio")

        assert "HELLO SERGIO" == text

    def test_change_text_to_lowercase_with_decorators(self):
        text = say_hello_in_lowercase_with_decorators("Sergio")

        assert "hello sergio" == text

    def test_change_text_to_uppercase_with_parametrized_decorator(self):
        text = say_hello_in_uppercase_with_parametrized_decorator("Sergio")

        assert "HELLO SERGIO" == text

    def test_change_text_to_lowercase_with_parametrized_decorator(self):
        text = say_hello_in_lowercase_with_parametrized_decorator("Sergio")

        assert "hello sergio" == text

    def test_not_change_text_with_invalid_argument_parametrized_decorator(self):
        with pytest.raises(Exception, match="Not valid type invalid"):
            say_hello_in_invalid_type_with_parametrized_decorator("Sergio")
