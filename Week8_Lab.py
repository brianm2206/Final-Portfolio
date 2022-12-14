# Brian Molina
# 12/13/2022
# Problem 1. Write a function that takes two inputs from a user
# and prints whether they are equal or not.
def check_equal():
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))
  if a == b:
    print("Numbers a and b are equal")
  elif a != b:
    print("Numbers a and b are not equal")
