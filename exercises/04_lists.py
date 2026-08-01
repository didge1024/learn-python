"""Warm-up 4 — Lists: holding many values in one place.

Run me:  python3 exercises/04_lists.py
"""

# A list holds a bunch of items, in order, inside square brackets:
fruits = ["apple", "banana", "cherry"]
print(f"My fruits: {fruits}")

# Get an item by its position (counting starts at 0!):
print(f"The first fruit is {fruits[0]}.")
print(f"The last fruit is {fruits[-1]}.")   # -1 means "the last one"

# How many items are in the list?
print(f"I have {len(fruits)} fruits.")

# Add a new item to the end:
fruits.append("date")
print(f"After adding one: {fruits}")

# Loop over every item in the list:
print("\nMy shopping list:")
for fruit in fruits:
    print(f"  - {fruit}")


# ---------------------------------------------------------------------------
# YOUR TURN
# 1. Make a list called `scores` with these numbers: 10, 20, 30, 40
# 2. Print how many scores there are.
# 3. Add the number 50 to the list.
# 4. Loop over the list and add them all up into a variable `total`,
#    then print the total.  (Hint: start with `total = 0` before the loop.)
#
# Write your code below:

