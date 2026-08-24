# DataDeck — Abstract Card Architecture

A small creature-battling card game used to explore three object-oriented design
patterns in Python. Each exercise removes a different `if/else` from the calling
code by hiding a decision behind an abstract class.

## Patterns

| Exercise | Pattern | Idea |
| --- | --- | --- |
| `ex0` | Abstract Factory | Each factory builds one **family** of creatures (base + evolved). Callers receive a factory and never name a concrete creature class. |
| `ex1` | Interface segregation | `HealCapability` and `TransformCapability` are pure interfaces. A creature inherits `Creature` for *what it is* and a capability for *what it can do*. |
| `ex2` | Strategy | The battle *routine* becomes its own object. The tournament calls `act()` and never asks what kind of creature it is holding. |

## Structure

```
ex0/          Creature hierarchy + CreatureFactory (FlameFactory, AquaFactory)
ex1/          Capability interfaces + HealingCreatureFactory, TransformCreatureFactory
ex2/          BattleStrategy + Normal/Aggressive/Defensive + InvalidStrategyError

battle.py     Tests the ex0 factories
capacitor.py  Tests the ex1 capabilities
tournament.py Round-robin tournament driving creatures through strategies
```

Each package exposes only its abstractions — `ex0` exports factories, never the
concrete `Flameling` or `Aquabub`.

## Running

Requires Python 3.9+. From the repository root:

```sh
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

## How a battle works

`tournament.py` holds a list of `(CreatureFactory, BattleStrategy)` pairs and runs a
round robin, so every opponent fights each other one exactly once:

- `NormalStrategy` — any creature — `attack`
- `AggressiveStrategy` — transform-capable — `transform` → `attack` → `revert`
- `DefensiveStrategy` — heal-capable — `attack` → `heal`

A strategy's `is_valid()` reports whether a creature suits it. Calling `act()` on a
mismatch raises `InvalidStrategyError`, which aborts the tournament with a clear
message.

Adding a new capability means writing a new interface, factory and strategy —
no existing file changes.

---

*This project was created as part of the 42 Python curriculum (Module 07).*
