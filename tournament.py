from ex0.CreatureFactory import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    fighters = []
    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            first, first_strategy = fighters[i]
            second, second_strategy = fighters[j]

            print()
            print("* Battle *")
            print(first.describe())
            print("vs.")
            print(second.describe())
            print("now fight!")

            try:
                messages = first_strategy.act(first) + second_strategy.act(second)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return

            for message in messages:
                print(message)


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])
