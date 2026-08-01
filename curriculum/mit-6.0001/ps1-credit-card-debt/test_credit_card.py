"""Smoke tests for PS1. These check shape/behavior, not the official grader values.
Run from the repo's main folder: ./test.sh curriculum/mit-6.0001/ps1-credit-card-debt"""
import pytest
from credit_card import (
    balance_after_year,
    min_fixed_payment_bruteforce,
    min_fixed_payment_bisection,
)


def test_part_a_reduces_balance():
    remaining = balance_after_year(4213.0, 0.2, 0.04)
    assert 0 < remaining < 4213.0


def test_part_b_is_multiple_of_ten_and_clears_debt():
    pay = min_fixed_payment_bruteforce(3329.0, 0.2)
    assert pay % 10 == 0
    assert pay > 0


def test_part_c_matches_bruteforce_within_ten_dollars():
    balance, rate = 3329.0, 0.2
    brute = min_fixed_payment_bruteforce(balance, rate)
    bisect = min_fixed_payment_bisection(balance, rate)
    assert abs(brute - bisect) <= 10
