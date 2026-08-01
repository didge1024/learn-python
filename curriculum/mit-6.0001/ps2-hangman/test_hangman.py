"""Smoke tests for the PS2 helper functions.
Run from the repo's main folder: ./test.sh curriculum/mit-6.0001/ps2-hangman"""
import string
from hangman import is_word_guessed, get_guessed_word, get_available_letters


def test_is_word_guessed():
    assert is_word_guessed("apple", ["a", "p", "l", "e"]) is True
    assert is_word_guessed("apple", ["a", "p", "l"]) is False


def test_get_guessed_word():
    assert get_guessed_word("apple", ["a", "l"]).replace(" ", "") == "a__l_"


def test_get_available_letters():
    remaining = get_available_letters(["a", "b", "c"])
    assert "a" not in remaining and "d" in remaining
    assert len(remaining) == len(string.ascii_lowercase) - 3
