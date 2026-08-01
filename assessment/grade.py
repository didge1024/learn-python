"""Self-directed placement diagnostic. Run: python3 grade.py

This is NOT a graded test — its only job is to find WHERE in the learning content
you should start. It routes you to the *first* level you can't fully clear: that gap
is your entry point. Everything below it, you already know; start there and move up."""
import assessment as a


def _check(fn):
    """Run a check; return True on pass, False on any exception or wrong answer."""
    try:
        return bool(fn())
    except Exception:
        return False


LEVELS = {
    "Level 1 — Fundamentals": [
        lambda: a.fizzbuzz(3) == "Fizz",
        lambda: a.fizzbuzz(5) == "Buzz",
        lambda: a.fizzbuzz(15) == "FizzBuzz",
        lambda: a.fizzbuzz(7) == "7",
        lambda: a.celsius_to_fahrenheit(100) == 212,
        lambda: a.celsius_to_fahrenheit(0) == 32,
    ],
    "Level 2 — Data structures": [
        lambda: a.word_count("a b a c a") == {"a": 3, "b": 1, "c": 1},
        lambda: a.word_count("") == {},
        lambda: tuple(sorted(a.two_sum([2, 7, 11, 15], 9))) == (0, 1),
        lambda: a.two_sum([1, 2, 3], 100) is None,
    ],
    "Level 3 — Functions & recursion": [
        lambda: a.fibonacci(0) == 0,
        lambda: a.fibonacci(1) == 1,
        lambda: a.fibonacci(10) == 55,
        lambda: a.flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5],
        lambda: a.flatten([]) == [],
    ],
    "Level 4 — Algorithms": [
        lambda: a.binary_search([1, 3, 5, 7, 9], 7) == 3,
        lambda: a.binary_search([1, 3, 5, 7, 9], 4) == -1,
        lambda: a.is_palindrome("A man, a plan, a canal: Panama") is True,
        lambda: a.is_palindrome("hello") is False,
    ],
    "Level 5 — OOP": [
        lambda: _run_stack(),
    ],
}


def _run_stack() -> bool:
    s = a.Stack()
    if not s.is_empty() or len(s) != 0:
        return False
    s.push(1)
    s.push(2)
    if len(s) != 2 or s.peek() != 2:
        return False
    if s.pop() != 2 or s.pop() != 1:
        return False
    return s.is_empty()


# For each level, WHERE to start in the available learning content if this is the
# first level you can't clear. Keyed by level index (0-based).
START_HERE = {
    0: (
        "Fundamentals — variables, loops, conditionals, strings",
        "MIT 6.0001, Problem Set 1 (Paying off credit-card debt)",
        "curriculum/mit-6.0001/ps1-credit-card-debt/",
    ),
    1: (
        "Data structures — dicts, lists, frequency counts",
        "MIT 6.0001, Problem Sets 2–3 (Hangman, Word Game)",
        "curriculum/mit-6.0001/ps2-hangman/  and  ps3-word-game/",
    ),
    2: (
        "Functions & recursion — decomposition, recursive thinking",
        "UC Berkeley CS61A (higher-order functions & recursion) — project 'Hog'",
        "curriculum/README.md  →  section 5 (CS61A), https://cs61a.org/",
    ),
    3: (
        "Algorithms — search, complexity, classic techniques",
        "MIT 6.006 Introduction to Algorithms",
        "curriculum/README.md  →  section 3, https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/",
    ),
    4: (
        "Object-oriented programming — classes, inheritance, polymorphism",
        "MIT 6.0001, Problem Set 5 (RSS feed filter) — or CS61A 'Ants'",
        "curriculum/mit-6.0001/ps5-rss-filter/",
    ),
}

# If you clear ALL levels, the diagnostic sends you past the language basics
# entirely, into the build-and-deploy track.
START_HERE_MASTERED = (
    "Systems & deployment — you've got the language; now learn to ship it",
    "Docker → Kubernetes track",
    "curriculum/README.md  →  section 6 (Docker Get Started, then Kubernetes Basics)",
)


def main() -> None:
    print("\n=== Placement Diagnostic — find where to start ===\n")
    first_gap = None
    for idx, (name, checks) in enumerate(LEVELS.items()):
        passed = sum(_check(c) for c in checks)
        total = len(checks)
        ok = passed == total
        if not ok and first_gap is None:
            first_gap = idx
        mark = "ok  " if ok else "GAP "
        print(f"[{mark}] {name}: {passed}/{total}")

    print("\n" + "-" * 60)
    if first_gap is None:
        topic, where, path = START_HERE_MASTERED
        print("You cleared every level. Skip the language basics.\n")
    else:
        topic, where, path = START_HERE[first_gap]
        print("Your first gap — and your starting point:\n")
    print(f"  Topic : {topic}")
    print(f"  Start : {where}")
    print(f"  Path  : {path}")
    print("-" * 60)
    print("\nThis is self-directed: work that content with Claude as your tutor,")
    print("then re-run this diagnostic to confirm the gap closed and move up.\n")


if __name__ == "__main__":
    main()
