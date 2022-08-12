"""Module containing the COFOG exception classes."""


from dataclasses import dataclass
from typing import Union


@dataclass
class InvalidCOFOGCodeError(Exception):
    """Raised when an invalid COFOG code is given."""

    code: Union[str, int]

    def __str__(self) -> str:
        """Returns the string representation of the exception."""
        message = f"{self.code} is not a valid COFOG code. \
            Valid COFOG codes start with numbers 1-10 and have 1 to 3 levels. \
            Please see the docs for more information."
        return message


@dataclass
class InvalidCOFOGLevelError(Exception):
    """Raised when an invalid COFOG level is given."""

    level: Union[str, int]

    def __str__(self) -> str:
        """Returns the string representation of the exception."""
        message = f"{self.level} is not a valid COFOG level. \
            Valid COFOG codes can only have levels 1, 2, or 3."
        return message
