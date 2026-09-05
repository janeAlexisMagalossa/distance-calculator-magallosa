# Reflection:
# Using the math library simplifies code by avoiding complex formulas from scratch.
# Functions like sqrt() and pow() make calculations direct, fast, and easy to read.

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"The distance between the two points is: {distance:.2f}")