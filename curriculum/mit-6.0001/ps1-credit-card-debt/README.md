# PS1 — Paying Off Credit-Card Debt

**Source:** MIT 6.0001, Problem Set 1 · https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/assignments/

## Goal

Three parts of increasing difficulty:

- **Part A — Balance after a year.** Given a balance, annual interest rate, and a fixed
  *fraction* paid each month, compute the remaining balance after 12 months.
- **Part B — Fixed minimum payment.** Find the smallest *fixed dollar* monthly payment
  (a multiple of $10) that pays the balance off within a year. Solve by brute force.
- **Part C — Bisection search.** Same as B, but find the answer with **bisection search**
  — dramatically fewer iterations. This is the real lesson.

## Skills

Loops, floating-point arithmetic, brute-force vs. binary search, converging on an answer.

## How to work it

1. Read the official PDF (link above) for exact numbers and expected output.
2. Fill in the functions in `credit_card.py`.
3. Run the tests: `python3 -m pytest` (from this folder).
4. When green, ask Claude to review your bisection loop for edge cases.
