"""Smoke tests for PS3.
Run from the repo's main folder: ./test.sh curriculum/mit-6.0001/ps3-word-game"""
from word_game import get_word_score, update_hand, is_valid_word


def test_word_score_basic():
    # 'cab' = c(3)+a(1)+b(3) = 7, times len 3 = 21 (no bonus, hand_size 7)
    assert get_word_score("cab", 7) == 21


def test_update_hand_removes_letters():
    hand = {"a": 1, "c": 1, "b": 1, "z": 1}
    new_hand = update_hand(hand, "cab")
    assert new_hand.get("z") == 1
    assert new_hand.get("a", 0) == 0


def test_is_valid_word():
    hand = {"c": 1, "a": 1, "b": 1}
    assert is_valid_word("cab", hand, ["cab", "dog"]) is True
    assert is_valid_word("dog", hand, ["cab", "dog"]) is False
