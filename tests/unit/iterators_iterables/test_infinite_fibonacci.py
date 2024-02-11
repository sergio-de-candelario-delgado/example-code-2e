from typing import List, Iterator, Iterable

import pytest

from iterators_iterables.infinite_fibonacci import FibonacciInfIterator


class TestInfiniteFibonacci:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.sut: FibonacciInfIterator = FibonacciInfIterator()

    def test_fibonacci_is_iterator_and_iterable_by_duck_typing(self):
        assert isinstance(self.sut, Iterator)
        assert isinstance(self.sut, Iterable)

        assert Iterator not in FibonacciInfIterator.mro()
        assert Iterable not in FibonacciInfIterator.mro()

    @pytest.mark.parametrize(
        "return_values, numbers", [
            ([0, 1, 1, 2, 3, 5], 5),
            ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 10),
            ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 15),
            ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181], 20),
        ]
    )
    def test_fibonacci_number_sequence(self, return_values: List[int], numbers: int):
        for i in range(0, numbers):
            assert next(self.sut) == return_values[i]
