class NumbersGenerator:

    def generate(self, numbers: int):
        for number in range(numbers):
            yield number
