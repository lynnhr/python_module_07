from ex0.CreatureFactory import CreatureFactory
from .Creature import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")
