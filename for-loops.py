"""
Complete the functions by replacing what's in `pass`.

Run this file to test.
"""


def implement_range(x: int) -> list[int]:
    """
    Return a list of integers in the interval [0, x). This includes 0 but
    excludes x.

    If x < 1, return an empty list.

    Don't use range, use a for loop!
    """
    pass


print("Testing implement_range")
assert implement_range(-5) == list(range(-5))
assert implement_range(0) == list(range(0))
assert implement_range(5) == list(range(5))
assert implement_range(8) == list(range(8))
assert implement_range(20) == list(range(20))


def implement_index(haystack: list[int], needle: int) -> int:
    """
    Implement list's index. Return the index of the needle in the haystack.

    Return -1 if not found.

    See the test cases for examples.
    """
    pass


print("Testing implement_index")
assert implement_index([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5].index(1)
assert implement_index([6, 7, 8, 4, 5], 1) == [6, 7, 8, 4, 5].index(1)
assert implement_index([10, 20, 30, 40, 50], 40) == [10, 20, 30, 40, 50].index(40)
assert implement_index([], 100) == [].index(1)


def get_pairs(x: str) -> list[str]:
    """
    Return a list of characters adjacent to each other.

    See the test cases for examples.
    """
    pass


print("Testing get_pairs")
assert get_pairs("a") == []
assert get_pairs("ab") == ["ab"]
assert get_pairs("abc") == ["ab", "bc"]
assert get_pairs("abcde") == ["ab", "bc", "cd", "de"]
