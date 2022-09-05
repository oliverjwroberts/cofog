"""Module containing the COFOG exception classes."""


import textwrap
from dataclasses import dataclass
from typing import Union


@dataclass
class InvalidCOFOGCodeError(Exception):
    """Raised when an invalid COFOG code is given."""

    code: Union[str, int]

    def __str__(self) -> str:
        """Returns the string representation of the exception."""
        message = f"""\
            {self.code} is not a valid COFOG code.
            Valid COFOG codes start with numbers 1-10 and have 1 to 3 levels.
            Please see the docs for more information.
            """
        return textwrap.dedent(message)


@dataclass
class InvalidCOFOGLevelError(Exception):
    """Raised when an invalid COFOG level is given."""

    level: Union[str, int]

    def __str__(self) -> str:
        """Returns the string representation of the exception."""
        message = f"""\
            {self.level} is not a valid COFOG level.
            Valid COFOG codes can only have 1, 2, or 3 levels.
            """
        return textwrap.dedent(message)


@dataclass
class NoParentError(Exception):
    """Raised when attempting to retrieve a parent of a level 1 code."""

    def __str__(self) -> str:
        """Returns the string representation of the exception."""
        message = """\
            Level 1 COFOGs do not have a parent.
            """
        return textwrap.dedent(message)


@dataclass
class NoChildrenError(Exception):
    """Raised when attempting to retrieve the children of non-parent code."""

    def __str__(self) -> str:
        """Returns the string representation of the exception."""
        message = """\
            The selected COFOG does not have any children.
            """
        return textwrap.dedent(message)
