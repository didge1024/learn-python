"""Smoke tests for PS4. Run: python3 -m pytest"""
from caesar import build_shift_dict, apply_shift


def test_build_shift_dict_wraps():
    d = build_shift_dict(1)
    assert d["a"] == "b"
    assert d["z"] == "a"
    assert d["Z"] == "A"


def test_apply_shift_preserves_non_letters():
    assert apply_shift("abc, xyz!", 1) == "bcd, yza!"


def test_shift_roundtrip():
    msg = "The quick brown fox."
    encrypted = apply_shift(msg, 7)
    assert apply_shift(encrypted, 26 - 7) == msg
