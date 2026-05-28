"""
aquarium.py — Aquarium Singleton
=================================
The Aquarium uses the Singleton design pattern to guarantee exactly one
aquarium instance exists throughout the application's lifetime.  This
reflects the real-world constraint that there is only ONE Auckland
Aquarium being managed.

The Singleton is implemented with a thread-safe metaclass so the pattern
works correctly even in multi-threaded contexts.
"""

import threading
from collections import Counter

from src.fish import Fish, FishFactory


# ──────────────────────────────────────────────
# Singleton metaclass
# ──────────────────────────────────────────────
class _SingletonMeta(type):
    """
    Thread-safe Singleton metaclass.

    The first time a class using this metaclass is instantiated, the
    instance is stored in ``_instances``.  Every subsequent call returns
    that same stored instance.
    """

    _instances: dict = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


# ──────────────────────────────────────────────
# Singleton product
# ──────────────────────────────────────────────
class Aquarium(metaclass=_SingletonMeta):
    """
    Singleton — represents the one Auckland Aquarium.

    Responsibilities
    ----------------
    * Accept fish additions via ``add_fish(species, count)``.
    * Delegate fish creation to ``FishFactory`` (Factory pattern).
    * Track stock counts and expose reporting helpers.
    * Allow fish removal for management operations.
    """

    def __init__(self, name: str = "Auckland Aquarium"):
        self.name = name
        # Maps species key → (Fish prototype, count)
        self._stock: dict[str, list[Fish]] = {}

    # ── Mutation ──────────────────────────────
    def add_fish(self, species: str, count: int = 1) -> None:
        """
        Add ``count`` fish of the given species to the aquarium.

        Uses FishFactory to create a representative Fish object and
        stores it alongside a running total.

        Parameters
        ----------
        species : str
            Species name recognised by FishFactory.
        count : int
            Number of fish to add (must be ≥ 1).

        Raises
        ------
        ValueError
            If species is unknown or count is less than 1.
        """
        if count < 1:
            raise ValueError("Count must be at least 1.")
        # Validate species via factory (raises ValueError if unknown)
        fish = FishFactory.create(species)
        key = species.strip().lower()
        if key not in self._stock:
            self._stock[key] = [fish, 0]
        self._stock[key][1] += count

    def remove_fish(self, species: str, count: int = 1) -> None:
        """
        Remove ``count`` fish of the given species from the aquarium.

        Raises
        ------
        ValueError
            If species not present or not enough fish available.
        """
        key = species.strip().lower()
        if key not in self._stock or self._stock[key][1] == 0:
            raise ValueError(f"No {species} currently in the aquarium.")
        available = self._stock[key][1]
        if count > available:
            raise ValueError(
                f"Cannot remove {count} {species}; only {available} available."
            )
        self._stock[key][1] -= count
        if self._stock[key][1] == 0:
            del self._stock[key]

    def clear(self) -> None:
        """Remove all fish (useful for testing / reset)."""
        self._stock.clear()

    # ── Query ─────────────────────────────────
    def total_fish(self) -> int:
        """Return the total number of fish across all species."""
        return sum(entry[1] for entry in self._stock.values())

    def species_count(self, species: str) -> int:
        """Return how many fish of a given species are in the aquarium."""
        return self._stock.get(species.strip().lower(), [None, 0])[1]

    def inventory(self) -> list[dict]:
        """
        Return a list of dicts describing current stock, sorted by species.

        Each dict has keys: species, category, habitat, count.
        """
        result = []
        for key in sorted(self._stock):
            fish_obj, count = self._stock[key]
            result.append(
                {
                    "species": fish_obj.name,
                    "category": fish_obj.category,
                    "habitat": fish_obj.habitat,
                    "count": count,
                }
            )
        return result

    def category_summary(self) -> dict[str, int]:
        """Return a mapping of category → total fish count."""
        summary: Counter = Counter()
        for fish_obj, count in self._stock.values():
            summary[fish_obj.category] += count
        return dict(summary)

    # ── Display ───────────────────────────────
    def display(self) -> str:
        """Return a formatted multi-line report of current inventory."""
        lines = [
            f"{'─' * 60}",
            f"  🐠  {self.name}  🐠",
            f"{'─' * 60}",
        ]
        if not self._stock:
            lines.append("  (aquarium is empty)")
        else:
            header = f"  {'Species':<14} {'Category':<32} {'Count':>5}"
            lines.append(header)
            lines.append(f"  {'─'*14} {'─'*32} {'─'*5}")
            for entry in self.inventory():
                lines.append(
                    f"  {entry['species']:<14} {entry['category']:<32} {entry['count']:>5}"
                )
            lines.append(f"{'─' * 60}")
            lines.append(f"  Total fish: {self.total_fish()}")
        lines.append(f"{'─' * 60}")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Aquarium(name={self.name!r}, total={self.total_fish()})"