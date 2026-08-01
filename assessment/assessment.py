"""Skills assessment — fill in each function, then run `python3 grade.py`.

Each function raises NotImplementedError until you complete it. Do them in order;
they get harder. Don't peek at solutions — the score only helps if it's honest.
"""
from __future__ import annotations  # lets modern type hints run on Python 3.9+

# ---------------------------------------------------------------------------
# Level 1 — Fundamentals
# ---------------------------------------------------------------------------


def fizzbuzz(n: int) -> str:
    """Return 'Fizz' if n divisible by 3, 'Buzz' if by 5, 'FizzBuzz' if both,
    otherwise the number as a string."""
    raise NotImplementedError


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Level 2 — Data structures
# ---------------------------------------------------------------------------


def word_count(text: str) -> dict[str, int]:
    """Return a dict mapping each whitespace-separated word to how many times it
    appears. Case-sensitive is fine."""
    raise NotImplementedError


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return the indices (i, j) of two numbers that add to target, or None."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Level 3 — Functions & recursion
# ---------------------------------------------------------------------------


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1)."""
    raise NotImplementedError


def flatten(nested: list) -> list:
    """Flatten an arbitrarily nested list of ints into a single flat list.
    e.g. [1, [2, [3, 4]], 5] -> [1, 2, 3, 4, 5]"""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Level 4 — Algorithms
# ---------------------------------------------------------------------------


def binary_search(sorted_nums: list[int], target: int) -> int:
    """Return the index of target in a sorted list, or -1 if absent. O(log n)."""
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """True if s reads the same forwards and backwards, ignoring case and any
    non-alphanumeric characters. 'A man, a plan, a canal: Panama' -> True."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Level 5 — OOP
# ---------------------------------------------------------------------------


class Stack:
    """A last-in-first-out stack. Implement push, pop, peek, is_empty, __len__."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, item) -> None:
        raise NotImplementedError

    def pop(self):
        """Remove and return the top item. Raise IndexError if empty."""
        raise NotImplementedError

    def peek(self):
        """Return (without removing) the top item. Raise IndexError if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
