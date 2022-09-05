"""Module containing parser functions for COFOG codes."""


import re
from typing import Dict
from typing import List
from typing import Optional

from cofog.data import COFOG_GLOSSARY
from cofog.exceptions import InvalidCOFOGCodeError
from cofog.types import COFOG_CODE_TYPE


def parse(code: COFOG_CODE_TYPE) -> str:
    """Function to parse the given COFOG code."""
    if not isinstance(code, str) and not isinstance(code, int):
        raise TypeError("COFOG code must be a string or integer.")

    # Handle case where str contains dots.
    if isinstance(code, str) and "." in code:
        if not bool(
            re.search(r"^(0[1-9]{1}|[1-9]{1}|10{1})(\.{1}\d{1}){0,2}$", code)
        ):  # noqa: W605
            raise InvalidCOFOGCodeError(code)
        # Append 0 at beginning if needed.
        if not code.startswith("0") and code[1] == ".":
            return "0" + code
        return code

    # Handle case where code is int or str with no dots.
    # Check code is between 1 and 4 digits, inclusive.
    if not 0 < len(str(code)) < 5:
        raise InvalidCOFOGCodeError(code)
    # Check code is a valid format.
    if not bool(
        re.search(r"^(0[1-9]{1}|[1-9]{1}|10{1})(\d{1}){0,2}$", str(code))
    ):  # noqa: W605
        raise InvalidCOFOGCodeError(code)
    # Parse code starting with 0
    if str(code).startswith("0"):
        return "0" + ".".join(str(code)[1:])
    # Parse code starting with 1
    if str(code).startswith("10"):
        return "1" + ".".join(str(code)[1:])
    # Parse code starting with other numbers
    return "0" + ".".join(str(code))


def get_level(code: str) -> int:
    """Function to get the level from the given COFOG code."""
    return code.count(".") + 1


def convert_to_lower_level(code: str, level: int) -> str:
    """Function to convert the given COFOG code to a lower level."""
    if level > get_level(code):
        raise ValueError("Level cannot be greater than the level of the code.")
    return ".".join(code.split(".")[:level])


def get_all_levels(code: str) -> Dict[int, Optional[str]]:  # noqa: D103
    """Function to get all levels from the given COFOG code."""
    level = get_level(code)
    if level == 1:
        level_one_code = code
        level_two_code = None
        level_three_code = None
    if level == 2:
        level_one_code = convert_to_lower_level(code, 1)
        level_two_code = code
        level_three_code = None
    if level == 3:
        level_one_code = convert_to_lower_level(code, 1)
        level_two_code = convert_to_lower_level(code, 2)
        level_three_code = code
    return {
        1: level_one_code,
        2: level_two_code,
        3: level_three_code,
    }


def filter_codes(code_to_test: str, code_reg_ex: str, level: int) -> bool:
    """Function to indicate if a code matches certain criteria.

    Args:
        code_to_test (str): Code to test the criteria on.
        code_reg_ex (str): RE pattern string to search for in code_to_test.
        level (int): Level of code being searched for.

    Returns:
        bool: Boolean indicator wether code_to_test passes the filter.
    """
    if bool(re.search(code_reg_ex, code_to_test)) and get_level(code_to_test) == level:
        return True
    return False


def get_children_of(parent_code: str) -> List[str]:
    """Get codes of the children of the current COFOG."""
    level = get_level(parent_code)
    child_level = level + 1
    children_codes = {
        code: desc
        for code, desc in COFOG_GLOSSARY.items()
        if filter_codes(code, parent_code, child_level)
    }
    return list(children_codes.keys())
