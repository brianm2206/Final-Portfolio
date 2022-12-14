# Brian Molina
# 12/13/2022
# Problem 2.  Write a function that takes two inputs from a user and
# prints whether the sum is greater than 10, less than 10, or equal to 10.

def sum_10():
  x = int(input("Enter a number: "))
  if x == 10:
    print("Number is equal to 10")
  elif x < 10:
    print("Number is less than 10")
  elif x > 10:
    print("Number is greater than 10")