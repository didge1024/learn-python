"""Warm-up 1 — Variables: giving names to values.

Run me:  python3 exercises/01_variables.py
"""

# A "variable" is a name that holds a value. Here are three:
name = "Alex"          # text (called a "string")
age = 12               # a whole number (an "int")
height_m = 1.5         # a number with a decimal (a "float")

# f-strings let you drop variables straight into text with { }:
print(f"Hi, I'm {name}. I'm {age} years old and {height_m} meters tall.")

# You can do math with number variables:
next_year = age + 1
print(f"Next year I'll be {next_year}.")

# You can join strings together too:
first = "Ada"
last = "Lovelace"
full_name = first + " " + last
print(f"The first programmer was {full_name}.")


# ---------------------------------------------------------------------------
# YOUR TURN
# 1. Change `name`, `age`, and `height_m` above to YOUR info and run the file.
# 2. Make a variable `favorite_food` with your favorite food as a string.
# 3. Print a sentence using it, like: "My favorite food is pizza."
#
# Write your code below this line, then run the file again:

