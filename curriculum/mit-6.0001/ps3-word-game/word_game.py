"""PS3 — Word Game. Implement scoring and hand management first."""

SCRABBLE_LETTER_VALUES = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1,
    "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
    "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10,
}


def get_word_score(word: str, hand_size: int) -> int:
    """Sum of letter values * len(word), plus a 50-point bonus if the word uses
    all `hand_size` letters. See the PDF for the exact formula."""
    raise NotImplementedError


def update_hand(hand: dict[str, int], word: str) -> dict[str, int]:
    """Return a NEW hand with the letters of `word` removed."""
    raise NotImplementedError


def is_valid_word(word: str, hand: dict[str, int], word_list: list[str]) -> bool:
    """True if `word` is in `word_list` AND can be spelled from `hand`."""
    raise NotImplementedError
