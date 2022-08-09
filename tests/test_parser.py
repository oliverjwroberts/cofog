"""Module to test the parser module."""


import pytest

from cofog.exceptions import InvalidCOFOGCodeError
from cofog.parser import convert_to_lower_level
from cofog.parser import get_all_levels
from cofog.parser import get_level
from cofog.parser import parse


class TestParser:
    """Class to test the parser module."""

    def test_parse_non_str_int(self) -> None:
        """Tests the parse method with a non-string/int code."""
        with pytest.raises(TypeError):
            parse([436])

    def test_parse_invalid_str_with_dots(self) -> None:
        """Tests the parse method with an invalid string code with dots."""
        with pytest.raises(InvalidCOFOGCodeError):
            parse("14.3.6")

    def test_parse_append_zero_to_str_with_dots(self) -> None:
        """Tests the parse method appends a zero to a string code with dots."""
        assert parse("4.3") == "04.3"

    def test_parse_invalid_length(self) -> None:
        """Tests the parse method with an invalid length code."""
        with pytest.raises(InvalidCOFOGCodeError):
            parse("04361")

    def test_parse_invalid_int(self) -> None:
        """Tests the parse method with an invalid integer code."""
        with pytest.raises(InvalidCOFOGCodeError):
            parse(8274)

    def test_parse_valid_code(self) -> None:
        """Tests the parse method with a valid COFOG code."""
        assert parse("1012") == "10.1.2"

    def test_get_level(self) -> None:
        """Tests the get_level method."""
        assert get_level("10.1.2") == 3

    def test_convert_to_lower_level_invalid_level(self) -> None:
        """Tests method raises error when level is > than the COFOG level."""
        with pytest.raises(ValueError):
            convert_to_lower_level("10.1", level=3)

    def test_convert_to_lower_level(self) -> None:
        """Tests the convert_to_lower_level method."""
        assert convert_to_lower_level("10.1.2", level=2) == "10.1"

    def test_get_all_levels_given_level_1(self) -> None:
        """Tests the get_all_levels method given a level 1 COFOG code."""
        assert get_all_levels("09") == {
            1: "09",
            2: None,
            3: None,
        }

    def test_get_all_levels_given_level_2(self) -> None:
        """Tests the get_all_levels method given a level 2 COFOG code."""
        assert get_all_levels("09.2") == {
            1: "09",
            2: "09.2",
            3: None,
        }

    def test_get_all_levels_given_level_3(self) -> None:
        """Tests the get_all_levels method given a level 3 COFOG code."""
        assert get_all_levels("09.2") == {
            1: "09",
            2: "09.2",
            3: "09.2.1",
        }
