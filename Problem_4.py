# Brian Molina
# 12/13/2022
# Problem 4. Write a function that takes a year as a parameter
# and returns True if the year is a leap year, False if it is otherwise.

def leap_year(year):
  if (year % 4) == 0: # Check for divisibilty by 4
    if (year % 100) == 0: # Check for divisibilty by 100
      if (year % 400) == 0: # Check for divisibilty by 400
        print(f"{year} is a leap year")
      else:
        print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")

  def check_equal():
    sum_10()
    print("\n")
    check_five([2,6,8,4,5])
    print("\n")
    leap_year(1994)
    print("\n")