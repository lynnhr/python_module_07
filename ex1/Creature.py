from ex0.Creature import Creature
from .HealCapability import HealCapability
from .TransformCapability import TransformCapability


class Sproutling(Creature, HealCapability):

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} uses Photosynthesis!"


class Bloomelle(Creature, HealCapability):

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} uses Healing Pollen!"


class Shiftling(Creature, TransformCapability):

    def __init__(self, name: str, type: str) -> None:
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} uses Shadow Strike!"
        return f"{self.name} uses Tackle!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a new form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} reverts to its original form!"


class Morphagon(Creature, TransformCapability):

    def __init__(self, name: str, type: str) -> None:
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} uses Chaos Beam!"
        return f"{self.name} uses Slam!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a new form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} reverts to its original form!"
