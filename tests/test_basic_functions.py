from random import shuffle
from typing import Dict, Union
from string import printable

import hypothesis.strategies as st
import pytest
from hypothesis import given, note

from rsokl_dummy.basic_functions import count_vowels, merge_max_mappings


##################################
# Basic implementations of tests #
##################################


def test_count_vowels_basic():
    # test basic strings with uppercase and lowercase letters
    assert count_vowels("aA bB yY", include_y=False) == 2
    assert count_vowels("aA bB yY", include_y=True) == 4

    # test empty strings
    assert count_vowels("", include_y=False) == 0
    assert count_vowels("", include_y=True) == 0


def test_merge_max_mappings():
    # test documented behavior
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 20, "c": -1}
    expected = {"a": 1, "b": 20, "c": -1}
    assert merge_max_mappings(dict1, dict2) == expected

    # test empty dict1
    dict1 = {}
    dict2 = {"a": 10.2, "f": -1.0}
    expected = dict2
    assert merge_max_mappings(dict1, dict2) == expected

    # test empty dict2
    dict1 = {"a": 10.2, "f": -1.0}
    dict2 = {}
    expected = dict1
    assert merge_max_mappings(dict1, dict2) == expected

    # test both empty
    dict1 = {}
    dict2 = {}
    expected = {}
    assert merge_max_mappings(dict1, dict2) == expected


###########################################
# Using pytest's parameterization feature #
###########################################


@pytest.mark.parametrize(
    "input_string, include_y, expected_count",
    [("aA bB yY", False, 2), ("aA bB yY", True, 4), ("", False, 0), ("", True, 0)],
)
def test_count_vowels_parameterized(
    input_string: str, include_y: bool, expected_count: int
):
    assert count_vowels(input_string, include_y) == expected_count


@pytest.mark.parametrize(
    "dict_a, dict_b, expected_merged",
    [
        (dict(a=1, b=2), dict(b=20, c=-1), dict(a=1, b=20, c=-1)),
        (dict(), dict(b=20, c=-1), dict(b=20, c=-1)),
        (dict(a=1, b=2), dict(), dict(a=1, b=2)),
        (dict(), dict(), dict()),
    ],
)
def test_merge_max_mappings_parameterized(
    dict_a: dict, dict_b: dict, expected_merged: dict
):
    assert merge_max_mappings(dict_a, dict_b) == expected_merged


####################
# Using Hypothesis #
####################


# a list of all printable non-vowel characters
_not_vowels = "".join([l for l in printable if l.lower() not in set("aeiouy")])


@given(
    not_vowels=st.text(alphabet=_not_vowels),
    vowels_but_not_ys=st.text(alphabet="aeiouAEIOU"),
    ys=st.text(alphabet="yY"),
)
def test_count_vowels_hypothesis(not_vowels: str, vowels_but_not_ys: str, ys: str):
    """
    Constructs an input string with a known number of:
       - non-vowel characters
       - non-y vowel characters
       - y characters
    and thus, by constructions, we can test that the output
    of `count_vowels` agrees with the known number of vowels
    """
    # list of characters
    letters = list(not_vowels) + list(vowels_but_not_ys) + list(ys)

    # We need to shuffle the ordering of our characters so that
    # our input string isn't unnaturally patterned; e.g. always
    # have its vowels at the end
    shuffle(letters)
    in_string = "".join(letters)

    # Hypothesis provides a `note` function that will print out
    # whatever input you give it, but only in the case that the
    # test fails.
    # This way we can see the exact string that we fed to `count_vowels`,
    # if it caused our test to fail
    note("in_string: " + in_string)

    # testing that `count_vowels` produces the expected output
    # both including and excluding y's in the count
    assert count_vowels(in_string, include_y=False) == len(vowels_but_not_ys)
    assert count_vowels(in_string, include_y=True) == len(vowels_but_not_ys) + len(ys)


@given(
    dict1=st.dictionaries(
        keys=st.integers(-10, 10) | st.text(), values=st.integers(-10, 10)
    ),
    dict2=st.dictionaries(
        keys=st.integers(-10, 10) | st.text(), values=st.integers(-10, 10)
    ),
)
def test_merge_max_mappings_hypothesis(
    dict1: Dict[Union[int, str], int], dict2: Dict[Union[int, str], int]
):
    merged_dict = merge_max_mappings(dict1, dict2)

    # property: `merged_dict` contains all of the keys among
    # `dict1` and `dict2`
    assert set(merged_dict) == set(dict1).union(
        dict2
    ), "novel keys were introduced or lost"

    # property: `merged_dict` only contains values that appear
    # among `dict1` and `dict2`
    assert set(merged_dict.values()) <= set(dict1.values()).union(
        dict2.values()
    ), "novel values were introduced"

    # property: `merged_dict` only contains key-value pairs with
    # the largest value represented among the pairs in `dict1`
    # and `dict2`
    assert all(dict1[k] <= merged_dict[k] for k in dict1) and all(
        dict2[k] <= merged_dict[k] for k in dict2
    ), "`merged_dict` contains a non-max value"

    # property: `merged_dict` only contains key-value pairs that
    # appear among `dict1` and `dict2`
    for k, v in merged_dict.items():
        assert (k, v) in dict1.items() or (
            k,
            v,
        ) in dict2.items(), "`merged_dict` did not preserve the key-value pairings"
