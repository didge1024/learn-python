"""Pytest view of the assessment — per-function pass/fail.
Run from the repo's main folder: ./test.sh assessment

These will fail until you implement the functions in assessment.py. That's expected:
turning them green IS the assessment."""
import pytest
import assessment as a


def test_fizzbuzz():
    assert a.fizzbuzz(3) == "Fizz"
    assert a.fizzbuzz(5) == "Buzz"
    assert a.fizzbuzz(15) == "FizzBuzz"
    assert a.fizzbuzz(7) == "7"


def test_celsius_to_fahrenheit():
    assert a.celsius_to_fahrenheit(100) == 212
    assert a.celsius_to_fahrenheit(0) == 32


def test_word_count():
    assert a.word_count("a b a c a") == {"a": 3, "b": 1, "c": 1}
    assert a.word_count("") == {}


def test_two_sum():
    assert tuple(sorted(a.two_sum([2, 7, 11, 15], 9))) == (0, 1)
    assert a.two_sum([1, 2, 3], 100) is None


def test_fibonacci():
    assert a.fibonacci(0) == 0
    assert a.fibonacci(10) == 55


def test_flatten():
    assert a.flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert a.flatten([]) == []


def test_binary_search():
    assert a.binary_search([1, 3, 5, 7, 9], 7) == 3
    assert a.binary_search([1, 3, 5, 7, 9], 4) == -1


def test_is_palindrome():
    assert a.is_palindrome("A man, a plan, a canal: Panama") is True
    assert a.is_palindrome("hello") is False


def test_stack():
    s = a.Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    with pytest.raises(IndexError):
        s.pop()
