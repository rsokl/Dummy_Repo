__all__ = ["count_vowels", "merge_max_mappings"]


def count_vowels(x, include_y=False):
    """Returns the number of vowels contained in `x`.
    The vowel 'y' is included optionally.

    Parameters
    ----------
    x : str
        The input string
    include_y : bool, optional (default=False)
        If `True` count y's as vowels

    Returns
    -------
    vowel_count: int

    Examples
    --------
    >>> count_vowels("happy")
    1
    >>> count_vowels("happy", include_y=True)
    2
    """
    vowels = set("aeiouAEIOU")
    if include_y:
        vowels.update("yY")
    return sum(1 for char in x if char in vowels)


def merge_max_mappings(dict1, dict2):
    """ Merges two dictionaries based on the largest value
    in a given mapping.

    Parameters
    ----------
    dict1 : Dict[str, float]
    dict2 : Dict[str, float]

    Returns
    -------
    merged : Dict[str, float]
        The dictionary containing all of the keys common
        between `dict1` and `dict2`, retaining the largest
        value from common mappings.

    Examples
    --------
    >>> x = {"a": 1, "b": 2}
    >>> y = {"b": 100, "c": -1}
    >>> merge_max_mappings(x, y)
    {'a': 1, 'b': 100, 'c': -1}
    """
    # `dict(dict1)` makes a copy of `dict1`. We do this
    # so that updating `merged` doesn't also update `dict1`
    merged = dict(dict1)
    for key, value in dict2.items():
        if key not in merged or value > merged[key]:
            merged[key] = value
    return merged
