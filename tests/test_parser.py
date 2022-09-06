"""Module to test the parser module."""


import pytest

from cofog.exceptions import InvalidCOFOGCodeError
from cofog.parser import convert_to_lower_level
from cofog.parser import filter_codes
from cofog.parser import get_all_levels
from cofog.parser import get_children_of
from cofog.parser import get_level
from cofog.parser import parse


class TestParseFunction:
    """Class to test the parse function."""

    def test_parse_non_str_int(self) -> None:
        """Tests the parse method with a non-string/int code."""
        with pytest.raises(TypeError):
            parse([436])  # type: ignore[arg-type]

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

    def test_parse_valid_zero_code(self) -> None:
        """Tests the parse method with a valid COFOG code starting with 0."""
        assert parse("0432") == "04.3.2"

    def test_parse_valid_non_zero_code(self) -> None:
        """Tests the method with a valid COFOG code not starting with 0."""
        assert parse("432") == "04.3.2"

    def test_parse_valid_ten_code(self) -> None:
        """Tests the parse method with a COFOG code starting with 10."""
        assert parse("10.1.2") == "10.1.2"

    def test_parse_valid_ten_code_no_dots(self) -> None:
        """Tests the method with a code starting with 10 and no dots."""
        assert parse("1012") == "10.1.2"


class TestParserLevelFunctions:
    """Class to test the parser level functions."""

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
        assert get_all_levels("09.2.1") == {
            1: "09",
            2: "09.2",
            3: "09.2.1",
        }


class TestParseChildren:
    """Class to test parent and children functionality."""

    def test_filter_codes_true(self) -> None:
        """Tests filter_codes method with a passing code."""
        assert filter_codes("07.3.2", r"7.3", 3) is True

    def test_filter_codes_false(self) -> None:
        """Tests filter_codes method with a non-passing code."""
        assert filter_codes("08.2", r"7.3", 3) is False

    def test_get_children_of(self) -> None:
        """Tests get_children_of method."""
        children_codes = ["07.3.1", "07.3.2", "07.3.3", "07.3.4"]
        assert get_children_of("07.3") == children_codes
