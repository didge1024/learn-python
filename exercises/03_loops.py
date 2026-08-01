"""Warm-up 3 — Loops: doing something many times without repeating yourself.

Run me:  python3 exercises/03_loops.py
"""

# A `for` loop repeats once for each item in a range.
print("Counting to 5:")
for number in range(1, 6):        # range(1, 6) gives 1, 2, 3, 4, 5
    print(number)

# You can loop over the letters of a word:
print("\nLetters in 'python':")
for letter in "python":
    print(letter)

# A `while` loop repeats as long as a condition stays True.
print("\nBlast off!")
countdown = 3
while countdown > 0:
    print(countdown)
    countdown = countdown - 1     # get closer to stopping each time
print("🚀 Lift off!")


# ---------------------------------------------------------------------------
# YOUR TURN
# 1. Use a for loop to print the numbers 1 through 10.
# 2. Then print only the EVEN numbers from 1 to 10.
#    Hint: `if number % 2 == 0:` is True when a number is even
#          (`%` gives the remainder after dividing).
#
# Write your loops below:

