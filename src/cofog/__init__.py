"""Cofog."""


import importlib.metadata

from cofog.cofog import COFOG  # noqa: F401


__version__ = importlib.metadata.version(__package__)
