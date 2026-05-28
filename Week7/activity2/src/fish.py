"""
fish.py — Fish domain models and Factory Pattern
=================================================
The FishFactory uses the Factory design pattern to create Fish objects
without exposing instantiation logic to the caller. The caller provides
a species name; the factory decides which concrete class to build.
"""

from abc import ABC, abstractmethod


# ──────────────────────────────────────────────
# Abstract product
# ──────────────────────────────────────────────
class Fish(ABC):
    """Abstract base class representing any fish in the aquarium."""

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def category(self) -> str:
        """Return the ecological / care category for this species."""

    @property
    @abstractmethod
    def habitat(self) -> str:
        """Return the preferred habitat zone."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"


# ──────────────────────────────────────────────
# Concrete products
# ──────────────────────────────────────────────
class Goldfish(Fish):
    @property
    def category(self) -> str:
        return "Freshwater – Ornamental"

    @property
    def habitat(self) -> str:
        return "Freshwater Tank"


class Shark(Fish):
    @property
    def category(self) -> str:
        return "Marine – Apex Predator"

    @property
    def habitat(self) -> str:
        return "Large Saltwater Tank"


class Angelfish(Fish):
    @property
    def category(self) -> str:
        return "Freshwater – Tropical"

    @property
    def habitat(self) -> str:
        return "Tropical Freshwater Tank"


class Tuna(Fish):
    @property
    def category(self) -> str:
        return "Marine – Pelagic"

    @property
    def habitat(self) -> str:
        return "Open Ocean Tank"


class Salmon(Fish):
    @property
    def category(self) -> str:
        return "Anadromous – Migratory"

    @property
    def habitat(self) -> str:
        return "Cold-Water Tank"


# ──────────────────────────────────────────────
# Factory
# ──────────────────────────────────────────────
class FishFactory:
    """
    Factory Pattern — centralises fish creation.

    The factory maps a species name (case-insensitive) to its concrete
    class.  Adding a new species only requires adding one entry here;
    no other code needs to change.
    """

    _registry: dict[str, type[Fish]] = {
        "goldfish": Goldfish,
        "shark": Shark,
        "angelfish": Angelfish,
        "tuna": Tuna,
        "salmon": Salmon,
    }

    @classmethod
    def create(cls, species: str) -> Fish:
        """
        Create and return a Fish instance for the given species name.

        Parameters
        ----------
        species : str
            The species name (e.g. "Goldfish", "shark").

        Returns
        -------
        Fish
            A concrete Fish subclass instance.

        Raises
        ------
        ValueError
            If the species is not registered in the factory.
        """
        key = species.strip().lower()
        fish_class = cls._registry.get(key)
        if fish_class is None:
            supported = ", ".join(cls.supported_species())
            raise ValueError(
                f"Unknown species: '{species}'. "
                f"Supported species: {supported}"
            )
        return fish_class(name=species.capitalize())

    @classmethod
    def supported_species(cls) -> list[str]:
        """Return a sorted list of all registered species names."""
        return sorted(cls._registry.keys())