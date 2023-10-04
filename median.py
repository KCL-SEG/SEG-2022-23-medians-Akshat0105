"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        numbers.sort()
        break
n = len(numbers)
if n%2 == 0:
    middleA = numbers[(n//2) -1]
    middleB = numbers[n//2]  
    median = (middleA + middleB) / 2         
else:
    median = numbers[n//2]        
print("Median :" , median)
