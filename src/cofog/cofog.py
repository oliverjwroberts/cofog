"""Module containing the COFOG class."""


from dataclasses import dataclass

from cofog.data import COFOG_GLOSSARY
from cofog.exceptions import InvalidCOFOGCodeError
from cofog.exceptions import InvalidCOFOGLevelError
from cofog.parser import get_all_levels
from cofog.parser import get_level
from cofog.parser import parse
from cofog.types import COFOG_CODE_TYPE


@dataclass
class COFOG:
    """A class to represent a COFOG.

    Raises:
        InvalidCOFOGCodeError: When an invalid COFOG code is given.
        InvalidCOFOGLevelError: When an invalid COFOG level is \
            specified in the set_level method.
        ValueError: When the specified level is higher than the \
            original level in the set_level method.

    Returns:
        cofog.COFOG: a COFOG class object.
    """

    code: COFOG_CODE_TYPE

    def __post_init__(self) -> None:
        """Method to run after initialisation of the COFOG class."""
        self.code = parse(self.code)
        if not self.is_valid():
            raise InvalidCOFOGCodeError(self.code)
        self.description = self.get_description()
        self.level = get_level(self.code)
        self._all_levels = get_all_levels(self.code)

    def __repr__(self) -> str:
        """Representation of the given COFOG."""
        return f"{self.code}: {self.description}"

    def is_valid(self) -> bool:
        """Determines whether the given COFOG is valid."""
        return self.code in COFOG_GLOSSARY

    def get_description(self) -> str:
        """Gets description of the given code."""
        return COFOG_GLOSSARY[str(self.code)]

    def set_level(self, level: int) -> None:
        """Sets the COFOG to the given level."""
        if not 0 < level < 4:
            raise InvalidCOFOGLevelError(level)
        if self._all_levels[level] is None:
            raise ValueError("Level does not exist for given COFOG code.")
        # Reset class attributes
        self.code = self._all_levels[level]  # type: ignore[assignment]
        self.description = self.get_description()
        self.level = get_level(str(self.code))
