"""Warm-up 2 — Conditionals: making decisions with if / elif / else.

Run me:  python3 exercises/02_conditionals.py
"""

# A conditional runs different code depending on whether something is True.
temperature = 30

if temperature > 25:
    print("It's hot — wear shorts! 🩳")
elif temperature > 10:
    print("It's mild — a t-shirt is fine. 👕")
else:
    print("It's cold — grab a jacket! 🧥")

# Comparisons give you True or False:
print(f"Is 5 bigger than 3? {5 > 3}")
print(f"Is 2 equal to 2? {2 == 2}")   # note: == means "is equal to"

# You can combine conditions with `and` / `or`:
age = 15
has_ticket = True
if age >= 13 and has_ticket:
    print("You can watch the movie. 🎬")
else:
    print("Sorry, you can't get in.")


# ---------------------------------------------------------------------------
# YOUR TURN
# Write a program that checks a `score` variable (0–100) and prints a grade:
#   90 or above  -> "A"
#   80 to 89     -> "B"
#   70 to 79     -> "C"
#   below 70     -> "Keep practicing!"
#
# Start by making a variable `score = 85`, then write your if/elif/else below:

