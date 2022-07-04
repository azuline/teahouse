"""
Complete the functions by replacing what's in `pass`.

Run this file to test.
"""


def greater_than_5(x: int) -> bool:
    """
    If x is greater than 5, return true. Otherwise false.
    """
    pass


print("Testing greater_than_5")
assert not greater_than_5(4)
assert not greater_than_5(5)
assert greater_than_5(6)


def dqs(x: float) -> int:
    """
    If x = 0, return 10.
    If x = 2, return 8.
    If x = 4, return 6.
    If x = 6, return 4.
    If x = 8, return 2.
    If x = 10, return 0.

    And round CORRECTLY, THANKS.
    """
    pass


print("Testing dqs")
assert dqs(0) == 10
assert dqs(1) == 8
assert dqs(2) == 8
assert dqs(3) == 7
assert dqs(4) == 6
assert dqs(5) == 4
assert dqs(6) == 4
assert dqs(7) == 2
assert dqs(8) == 2
assert dqs(9) == 0
assert dqs(10) == 0


def is_shorter(x: str, y: str) -> str:
    """
    Return the shorter string. If both are equal length, return the string
    which is lexographicallye first.
    """
    pass


print("Testing is_shorter")
assert is_shorter("a", "aa") == "a"
assert is_shorter("bb", "aa") == "aa"
assert is_shorter("bb", "aaa") == "bb"
