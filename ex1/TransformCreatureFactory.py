from ex0.CreatureFactory import CreatureFactory

from .Creature import Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
