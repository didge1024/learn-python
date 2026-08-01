# PS3 — Word Game (Scrabble-style)

**Source:** MIT 6.0001, Problem Set 3 · https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/assignments/

## Goal

Build a Scrabble-like word game:

1. **`get_word_score`** — score a word by its letters and length bonus.
2. **`deal_hand` / `update_hand` / `is_valid_word`** — manage a hand of letters.
3. **`play_hand` / `play_game`** — human play loop.
4. **Extension: a computer player** that picks the highest-scoring valid word.

## Skills

Dictionaries, frequency counts, scoring rules, breaking a problem into functions.

## How to work it

1. Read the official PDF for the exact scoring rules and letter values.
2. Implement scoring + hand management first (the tests hit these).
3. Add the interactive loops, then the computer player as a stretch goal.
