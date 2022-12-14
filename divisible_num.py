#Brian Molina
#11/10/10

# print numbers and states if a number is divisible.

for i in range(1, 51):
    print(i, end=": ")
    if i % 3 == 0:
        print("Divisible by 3")
    elif i % 5 == 0:
        print("Divisible by 5")
    elif i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
else:
        print()