#Brian Molina
#11/25/2022

# Problem 4.Write a Python function that takes a list
# of numbers and returns a new list with
# unique elements of the first list

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))