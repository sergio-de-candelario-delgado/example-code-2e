from data_model.vector2d import Vector


class TestVectors:

    def test_vector_sum(self):
        vector_1 = Vector(1, 2)
        vector_2 = Vector(3, 4)

        combination = vector_1 + vector_2

        assert combination == Vector(4, 6)

    def test_vector_abs(self):
        vector = Vector(3, 4)

        assert abs(vector) == 5

    def test_vector_multiply(self):
        vector = Vector(3, 4)
        multiplied_vector = vector * 3

        assert multiplied_vector == Vector(9, 12)
        assert abs(multiplied_vector) == 15

    def test_to_string(self):
        vector = Vector(1, 2)

        assert 'Vector(1, 2)' == str(vector)
