from typing import Generator

import pytest

from generators.numbers_generator import NumbersGenerator


class TestNumbersGenerator:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.sut = NumbersGenerator()

    def test_result_is_a_generator(self):
        result = self.sut.generate(10)
        assert isinstance(result, Generator)

    def test_generate_bit_amount_of_numbers_without_memory_overflow(self):
        numbers: int = 10000000
        result = self.sut.generate(numbers)
        total_records: int = 0

        for _ in result:
            total_records += 1

        assert total_records == numbers

    def test_create_list_from_generator(self):
        numbers: int = 10
        result = self.sut.generate(numbers)
        result_list = list(result)

        assert len(result_list) == numbers
        assert result_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

