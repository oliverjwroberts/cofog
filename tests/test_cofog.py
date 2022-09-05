"""Module to test the COFOG module."""


import pytest

from cofog.cofog import COFOG
from cofog.exceptions import InvalidCOFOGCodeError
from cofog.exceptions import InvalidCOFOGLevelError
from cofog.exceptions import NoChildrenError
from cofog.exceptions import NoParentError


class TestCOFOG:
    """Class to test the COFOG class methods."""

    def test_representation(self) -> None:
        """Tests the representation method."""
        assert repr(COFOG("04.4")) == "04.4: Mining, manufacturing and construction"

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


class TestSetLevel:
    """Class to test the set_level method."""

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
        assert cofog.code == "04.3"

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
        assert cofog.code == "04.3.6"


class TestParentChild:
    """Class to test the get parent and children functionality."""

    def test_get_parent_code_error(self) -> None:
        """Tests error raised when getting parents of level 1 code."""
        cofog = COFOG("4")
        with pytest.raises(NoParentError):
            cofog.get_parent_code()

    def test_get_parent_code(self) -> None:
        """Tests get_parent_code method."""
        cofog = COFOG("6.3")
        assert cofog.get_parent_code() == "06"

    def test_get_children_codes_error(self) -> None:
        """Tests error raised when getting children of level 3 code."""
        cofog = COFOG("07.3.2")
        with pytest.raises(NoChildrenError):
            cofog.get_children_codes()

    def test_get_children_codes(self) -> None:
        """Tests get_children_codes method."""
        cofog = COFOG("7.3")
        children_codes = ["07.3.1", "07.3.2", "07.3.3", "07.3.4"]
        assert cofog.get_children_codes() == children_codes
