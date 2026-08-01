# PS2 — Hangman

**Source:** MIT 6.0001, Problem Set 2 · https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/assignments/

## Goal

Build the word-guessing game Hangman, in stages:

1. **Helper functions** — `is_word_guessed`, `get_guessed_word`, `get_available_letters`.
2. **`hangman(secret_word)`** — the full game loop: limited guesses, warnings for
   repeats/invalid input, feedback each turn, win/lose messages.
3. **Extension: `hangman_with_hints`** — reveal possible matching words on request.

## Skills

Strings, loops, conditionals, user input, tracking game state, decomposition.

## How to work it

1. Read the official PDF for exact rules (guess count, warnings, scoring).
2. Implement the helpers first — the tests target those.
3. Wire up `hangman()` and play it: `python3 hangman.py`.
4. Ask Claude to review your game loop for readability and edge cases.
