"""Module to test the COFOG module."""


import pytest

from cofog.cofog import COFOG
from cofog.exceptions import InvalidCOFOGCodeError
from cofog.exceptions import InvalidCOFOGLevelError


class TestCOFOG:
    """Class to test the COFOG class methods."""

    def test_is_valid_str(self) -> None:
        """Tests the is_valid method with a string code."""
        assert COFOG("7.2.4").is_valid()

    def test_is_invalid_str(self) -> None:
        """Tests the is_valid method with an invalid string code."""
        with pytest.raises(InvalidCOFOGCodeError):
            COFOG("02.3.5")

    def test_is_valid_int(self) -> None:
        """Tests the is_valid method with an integer code."""
        assert COFOG(421).is_valid()

    def test_is_invalid_int(self) -> None:
        """Tests the is_valid method with an invalid integer code."""
        with pytest.raises(InvalidCOFOGCodeError):
            COFOG(827)

    def test_description(self) -> None:
        """Tests the description method."""
        assert COFOG("04.4").description == "Mining, manufacturing and construction"

    def test_set_level_raises_error(self) -> None:
        """Tests method raises error when to high/low level is specified."""
        cofog = COFOG("4.3.6")
        with pytest.raises(InvalidCOFOGLevelError):
            cofog.set_level(4)

    def test_set_level_not_specified(self) -> None:
        """Tests method raises error when level 2 code is set to level 3."""
        cofog = COFOG("4.3")
        with pytest.raises(ValueError):
            cofog.set_level(3)

    def test_set_level_code(self) -> None:
        """Tests the set_level method sets the correct code."""
        cofog = COFOG("4.3.6")
        cofog.set_level(2)
        assert cofog.code == "4.3"

    def test_set_level_description(self) -> None:
        """Tests the set_level method sets the correct description."""
        cofog = COFOG("4.3.6")
        cofog.set_level(2)
        assert cofog.description == "Fuel and energy"

    def test_set_level_level(self) -> None:
        """Tests the set_level method sets the correct level."""
        cofog = COFOG("4.3.6")
        cofog.set_level(2)
        assert cofog.level == 2

    def test_set_higher_level(self) -> None:
        """Tests method returns original code after being set to lower level."""
        cofog = COFOG("4.3.6")
        cofog.set_level(1)
        cofog.set_level(3)
        assert cofog.code == "4.3.6"
