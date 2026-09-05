#allows usage of math.sqrt and math.pow
import math

#sets up the values
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#prepares the formula for solving
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#displays the final answer
print(f"The distance between the two points is: {distance:.2f}")
