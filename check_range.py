#Brian Molina
#11/25/2022

# Problem 2.Write a Python function to check whether a 
# number is between 1 and 10. The
# function should take a number as a 
# parameter and return True if the number is between 1 and 
# 10, and False if the number is not between 1 and 10
import math
def test_range(n):
    if n in range(3,9):
        print(" %s is in the range%", str(n))
    else:
        print("The number is outside the range.")