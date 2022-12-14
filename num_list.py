#Brian Molina
#11/10/10

#prints the number and it's square.

nums = [12,10,32,3,66,17,42,99,20]
for i in nums:
    squared = []

for i in nums:
    sqr = i * i
    squared.append(sqr)
    print("The square of {} is {}".format(i,sqr))
