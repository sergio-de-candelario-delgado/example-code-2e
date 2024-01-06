from inheritance.animals import Mammal, Flying, Swimmer, Penguin


class TestDecoratorsAsFunctions:

    def test_mammal_animal(self):
        animal = Mammal.with_default_name()

        assert "Mammal" == animal.name

        assert animal.walking is False

        animal.start_walking()

        assert animal.walking is True

        animal.stop_walking()

        assert animal.walking is False

    def test_flying_animal(self):
        animal = Flying.with_default_name()

        assert "Flying" == animal.name

        assert animal.flying is False

        animal.start_flying()

        assert animal.flying is True

        animal.stop_flying()

        assert animal.flying is False

    def test_swimmer_animal(self):
        animal = Swimmer.with_default_name()

        assert "Swimmer" == animal.name

        assert animal.swimming is False

        animal.start_swimming()

        assert animal.swimming is True

        animal.stop_swimming()

        assert animal.swimming is False

    def test_penguin_animal(self):
        animal = Penguin.with_default_name()

        assert "Pingu the penguin!!!" == animal.name

        assert animal.walking is False
        assert animal.swimming is False

        animal.start_walking()
        animal.start_swimming()

        assert animal.walking is True
        assert animal.swimming is True

        animal.stop_walking()
        animal.stop_swimming()

        assert animal.walking is False
        assert animal.swimming is False



