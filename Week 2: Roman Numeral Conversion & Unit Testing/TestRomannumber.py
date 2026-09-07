import pytest
from roman import roman_to_integer
@pytest.mark.parametrize("roman, expected", [
    ("I", 1),
    ("VI", 6),
    ("XVI", 16),
    ("IV", 4),
    ("IX", 9),
    ("MD", 1500),
    ("MMMCMXCIX", 3999),
])
def test_roman_to_integer(roman, expected):
    assert roman_to_integer(roman) == expected


def test_roman_to_integer_accepts_lowercase():
    assert roman_to_integer("mmxxvi") == 2026


@pytest.mark.parametrize("roman", [
    "",
    "IIII",
    "XXXX",
    "CCCC",
    "MMMM",
    "VV",
    "LL",
    "DD",
    "ABC",
    "IIV",
    "IIX",
    "VX",
    "XDD",
    "CMCC",
    "MCMC",
    "MMMMCMXCIX",
])
def test_invalid_roman(roman):
    with pytest.raises(ValueError):
        roman_to_integer(roman)
