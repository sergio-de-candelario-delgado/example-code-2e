from abc import ABC


class Animal(ABC):
    def __init__(self, name: str):
        self.name: str = name


class Mammal(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.walking: bool = False

    @classmethod
    def with_default_name(cls):
        return cls(name="Mammal")

    def start_walking(self) -> None:
        self.walking = True

    def stop_walking(self) -> None:
        self.walking = False


class Flying(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.flying: bool = False

    @classmethod
    def with_default_name(cls):
        return cls(name="Flying")

    def start_flying(self) -> None:
        self.flying = True

    def stop_flying(self) -> None:
        self.flying = False


class Swimmer(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.swimming: bool = False

    @classmethod
    def with_default_name(cls):
        return cls(name="Swimmer")

    def start_swimming(self) -> None:
        self.swimming = True

    def stop_swimming(self) -> None:
        self.swimming = False


class Penguin(Mammal, Swimmer):

    @classmethod
    def with_default_name(cls):
        return cls(name="Pingu the penguin!!!")
