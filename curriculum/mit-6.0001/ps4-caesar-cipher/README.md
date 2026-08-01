# PS4 — Caesar Cipher

**Source:** MIT 6.0001, Problem Set 4 · https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/assignments/

## Goal

1. **`build_shift_dict`** — map every letter to its shifted counterpart (wrapping z→a).
2. **`apply_shift`** — encrypt/decrypt a message, leaving punctuation and spaces alone.
3. **`decrypt_message`** — you don't know the shift, so **try all 26** and pick the one
   that produces the most real English words. This is a brute-force attack.

## Skills

String manipulation, dictionaries, modular arithmetic, brute-force cracking.

## How to work it

1. Read the official PDF (case handling, non-letters pass through unchanged).
2. Implement `build_shift_dict` and `apply_shift` (tests target these).
3. Add `decrypt_message` using a word list to score candidate decryptions.
