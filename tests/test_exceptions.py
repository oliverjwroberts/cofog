"""Module to test the exceptions module."""


import textwrap

from cofog.exceptions import InvalidCOFOGCodeError
from cofog.exceptions import InvalidCOFOGLevelError
from cofog.exceptions import NoChildrenError
from cofog.exceptions import NoParentError


class TestCOFOGExceptions:
    """Class to test the COFOG exceptions."""

    def test_cofog_code_error_str(self) -> None:
        """Tests the string representation of the COFOG code error."""
        error = InvalidCOFOGCodeError("11.1.1")
        message = """\
            11.1.1 is not a valid COFOG code.
            Valid COFOG codes start with numbers 1-10 and have 1 to 3 levels.
            Please see the docs for more information.
            """
        assert str(error) == textwrap.dedent(message)

    def test_cofog_level_error_str(self) -> None:
        """Tests the string representation of the COFOG level error."""
        error = InvalidCOFOGLevelError("4")
        message = """\
            4 is not a valid COFOG level.
            Valid COFOG codes can only have 1, 2, or 3 levels.
            """
        assert str(error) == textwrap.dedent(message)

    def test_no_parent_error_str(self) -> None:
        """Tests the string representation of the No Parent error."""
        error = NoParentError()
        message = """\
            Level 1 COFOGs do not have a parent.
            """
        assert str(error) == textwrap.dedent(message)

    def test_no_children_error_str(self) -> None:
        """Tests the string representation of the No Children error."""
        error = NoChildrenError()
        message = """\
            The selected COFOG does not have any children.
            """
        assert str(error) == textwrap.dedent(message)
