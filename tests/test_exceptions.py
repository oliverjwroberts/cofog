"""Module to test the exceptions module."""


from cofog.exceptions import InvalidCOFOGCodeError
from cofog.exceptions import InvalidCOFOGLevelError


class TestCOFOGExceptions:
    """Class to test the COFOG exceptions."""

    def test_cofog_code_error_str(self) -> None:
        """Tests the string representation of the COFOG code error."""
        error = InvalidCOFOGCodeError("11.1.1")
        assert (
            str(error)
            == "11.1.1 is not a valid COFOG code. \
            Valid COFOG codes start with numbers 1-10 and have 1 to 3 levels. \
            Please see the docs for more information."
        )

    def test_cofog_level_error_str(self) -> None:
        """Tests the string representation of the COFOG level error."""
        error = InvalidCOFOGLevelError("4")
        assert (
            str(error)
            == "4 is not a valid COFOG level. \
            Valid COFOG codes can only have levels 1, 2, or 3."
        )
