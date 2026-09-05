# distance-calculator-magallosa
#it calculates distance 
# to run the program, just input what values you want for x1, y1, x2, y2
# the inputs are x1 for the x coordinate of the first value, y1 for the y coordinate of the first value, x2 for the x coordinate of the second value, and y2 for the y coordinate of the second value
#import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"The distance between the two points is: {distance:.2f}")

#janne alexys c. magallosa
#8-Sampaguita

