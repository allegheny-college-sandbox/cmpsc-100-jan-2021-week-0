#!/usr/bin/env python3

# IGNORE THIS #
def open_box(combo):
    vals = [2, 3, 6]
    pts = [a * b for a, b in zip(vals, combo)]
    return sum(pts)
# IGNORE THIS #

# Set up counter
counter = 0

# Set up message
message = "🎉🎉🎉You've opened the puzzle box!🎉🎉🎉"

# Initial state of buttons
buttons = [False, False, False]

# Space to try combinations; keep in mind that you will change values one at a time by assigning them

# TODO

result = open_box(buttons)

# If the value of result is exactly 5, print the value of message

# TODO