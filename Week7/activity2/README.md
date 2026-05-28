# 🐠 Auckland Aquarium Management System

> **Week 7 – Activity 2 | Design Patterns in Project Implementation**  
> Demonstrates the **Factory** and **Singleton** design patterns in a fish-management system for an aquarium in Auckland, New Zealand.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Species & Categories](#species--categories)
3. [Design Patterns](#design-patterns)
   - [Factory Pattern](#factory-pattern)
   - [Singleton Pattern](#singleton-pattern)
4. [Project Structure](#project-structure)
5. [Getting Started](#getting-started)
6. [Running the CLI](#running-the-cli)
7. [Running Tests](#running-tests)
8. [UML Class Diagram](#uml-class-diagram)
9. [Sample Output](#sample-output)

---

## Project Overview

The Auckland Aquarium Management System lets staff:

- **Add** fish to the aquarium by species and quantity
- **Remove** fish from the aquarium
- **View** a full inventory showing each species, its ecological category, habitat type, and current count
- **Summarise** stock by category

The system manages five species: **Goldfish, Shark, Angelfish, Tuna, and Salmon**.

---

## Species & Categories

| Species    | Category                    | Habitat                  |
|------------|-----------------------------|--------------------------|
| Goldfish   | Freshwater – Ornamental     | Freshwater Tank          |
| Shark      | Marine – Apex Predator      | Large Saltwater Tank     |
| Angelfish  | Freshwater – Tropical       | Tropical Freshwater Tank |
| Tuna       | Marine – Pelagic            | Open Ocean Tank          |
| Salmon     | Anadromous – Migratory      | Cold-Water Tank          |

---

## Design Patterns

### Factory Pattern

**Location:** `src/fish.py` — `FishFactory` class

**Why it's appropriate here:**  
The aquarium needs to create different types of fish objects based on a species name supplied at runtime (e.g. from user input or a database). Without the Factory pattern, the caller would need to know every concrete class and choose which `if`/`elif` branch to take — tightly coupling business logic to fish constructors.

`FishFactory.create(species)` hides all of that complexity behind a single method call.

**How it works:**

```
User Input "goldfish"
      │
      ▼
FishFactory.create("goldfish")
      │  looks up _registry dict
      ▼
  Goldfish()   ← concrete class chosen by the factory
      │
      ▼
  Fish object returned to caller
```

**Key code:**

```python
class FishFactory:
    _registry = {
        "goldfish":  Goldfish,
        "shark":     Shark,
        "angelfish": Angelfish,
        "tuna":      Tuna,
        "salmon":    Salmon,
    }

    @classmethod
    def create(cls, species: str) -> Fish:
        key = species.strip().lower()
        fish_class = cls._registry.get(key)
        if fish_class is None:
            raise ValueError(f"Unknown species: '{species}'")
        return fish_class(name=species.capitalize())
```

**Benefits:**
- Adding a new species only requires one line in `_registry` — no other code changes.
- Decouples fish creation from business logic.
- Validates species names in a single place.

---

### Singleton Pattern

**Location:** `src/aquarium.py` — `Aquarium` class (via `_SingletonMeta` metaclass)

**Why it's appropriate here:**  
There is physically **one** Auckland Aquarium. Allowing multiple `Aquarium` instances would mean two parts of the application could hold contradictory stock counts. The Singleton guarantees a single, consistent source of truth.

**How it works:**

```
First call:  Aquarium()  →  creates instance  →  stores in _instances
Second call: Aquarium()  →  finds instance in _instances  →  returns same object
```

**Key code:**

```python
class _SingletonMeta(type):
    _instances: dict = {}
    _lock = threading.Lock()          # thread-safe

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Aquarium(metaclass=_SingletonMeta):
    ...
```

**Proof in code (`main.py`):**
```python
aquarium      = Aquarium()   # creates the instance
same_instance = Aquarium()   # returns the SAME object
assert id(same_instance) == id(aquarium)   # ✅ always passes
```

**Benefits:**
- Prevents inconsistent state from multiple aquarium objects.
- Thread-safe — safe to use in multi-threaded environments.
- Global access point without global variables.

---

### Why Both Patterns Together?

| Concern | Pattern Used | Reason |
|---|---|---|
| *How many aquariums?* | **Singleton** | Only one real aquarium exists |
| *How are fish objects made?* | **Factory** | Species determined at runtime; creation logic centralised |

The two patterns are complementary: the Singleton manages the *one aquarium*, and the Factory creates the *many fish* that live inside it.

---

## Project Structure

```
aquarium-auckland/
│
├── src/
│   ├── __init__.py          # public API exports
│   ├── fish.py              # Fish base class, 5 concrete classes, FishFactory
│   └── aquarium.py          # _SingletonMeta metaclass + Aquarium Singleton
│
├── main.py                  # Interactive CLI entry point
└── README.md
```

---

## Running the CLI

```bash
python main.py
```

The CLI pre-loads a realistic starting inventory and presents a numbered menu:

```
1. Add fish
2. Remove fish
3. View inventory
4. View category summary
5. Exit
```

---

## UML Class Diagram

```
          ┌──────────────────────────────┐
          │       «metaclass»            │
          │       _SingletonMeta         │
          │──────────────────────────────│
          │ _instances: dict             │
          │ _lock: Lock                  │
          │ __call__()                   │
          └──────────────┬───────────────┘
                         │ metaclass
          ┌──────────────▼───────────────┐
          │         Aquarium             │  ← Singleton
          │──────────────────────────────│
          │ name: str                    │
          │ _stock: dict                 │
          │──────────────────────────────│
          │ add_fish(species, count)     │
          │ remove_fish(species, count)  │
          │ inventory() → list[dict]     │
          │ category_summary() → dict    │
          │ display() → str              │
          └──────────────────────────────┘
                         │ uses
          ┌──────────────▼───────────────┐
          │        FishFactory           │  ← Factory
          │──────────────────────────────│
          │ _registry: dict              │
          │──────────────────────────────│
          │ create(species) → Fish       │
          │ supported_species() → list   │
          └──────────────┬───────────────┘
                         │ creates
          ┌──────────────▼───────────────┐
          │        «abstract»            │
          │           Fish               │
          │──────────────────────────────│
          │ name: str                    │
          │ category: str  «abstract»    │
          │ habitat: str   «abstract»    │
          └──┬──────┬────┬──────┬───────┘
             │      │    │      │
         Goldfish Shark Angelfish Tuna Salmon
```

---

## Sample Output

```
────────────────────────────────────────────────────────────
  🐠  Auckland Aquarium  🐠
────────────────────────────────────────────────────────────
  Species        Category                          Count
  ────────────── ──────────────────────────────── ─────
  Angelfish      Freshwater – Tropical                 8
  Goldfish       Freshwater – Ornamental              12
  Salmon         Anadromous – Migratory                7
  Shark          Marine – Apex Predator                2
  Tuna           Marine – Pelagic                      5
────────────────────────────────────────────────────────────
  Total fish: 34
────────────────────────────────────────────────────────────
```

---

## Author

Auckland Aquarium Management System — Week 7, Activity 2  
*Design Patterns: Factory + Singleton*