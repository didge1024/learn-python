"""PS4 — Caesar cipher. Non-letters pass through unchanged; case is preserved."""
import string


def build_shift_dict(shift: int) -> dict[str, str]:
    """Map each lower- and upper-case letter to the letter `shift` positions later,
    wrapping around the alphabet. Non-letters are not included."""
    raise NotImplementedError


def apply_shift(message: str, shift: int) -> str:
    """Return `message` with each letter shifted by `shift` (use build_shift_dict)."""
    raise NotImplementedError


def decrypt_message(encrypted: str, word_list: list[str]) -> tuple[int, str]:
    """Try all 26 shifts; return (best_shift, best_plaintext) — the decryption with
    the most words found in word_list."""
    raise NotImplementedError


if __name__ == "__main__":
    print(apply_shift("Hello, World!", 3))
