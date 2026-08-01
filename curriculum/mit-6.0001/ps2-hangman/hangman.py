"""PS2 — Hangman. Implement the helpers, then the game loop."""
import random

SECRET_WORDS = ["apple", "banana", "python", "orchestra", "container"]


def is_word_guessed(secret_word: str, letters_guessed: list[str]) -> bool:
    """True if every letter of secret_word is in letters_guessed."""
    raise NotImplementedError


def get_guessed_word(secret_word: str, letters_guessed: list[str]) -> str:
    """Return secret_word with un-guessed letters shown as '_ ' (e.g. 'a_ _ le')."""
    raise NotImplementedError


def get_available_letters(letters_guessed: list[str]) -> str:
    """Return the alphabet with guessed letters removed."""
    raise NotImplementedError


def hangman(secret_word: str) -> None:
    """Full interactive game. See the official PDF for exact rules."""
    raise NotImplementedError


if __name__ == "__main__":
    hangman(random.choice(SECRET_WORDS))
