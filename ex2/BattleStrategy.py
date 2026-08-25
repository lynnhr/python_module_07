from abc import ABC, abstractmethod
from ex0.Creature import Creature
from ex1.HealCapability import HealCapability
from ex1.TransformCapability import TransformCapability
from .InvalidStrategyError import InvalidStrategyError


class BattleStrategy(ABC):

    name: str = "battle"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    def _reject_invalid(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this {self.name} strategy"
            )


class NormalStrategy(BattleStrategy):

    name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        self._reject_invalid(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        self._reject_invalid(creature)
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):

    name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        self._reject_invalid(creature)
        return [creature.attack(), creature.heal()]
