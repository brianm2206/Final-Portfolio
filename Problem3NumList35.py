#Brian Molina
#December 6, 2022

#Problem 3. Using a while loop, ask the user to enter a number. Append each entered number
#to a list and add them together. Continue asking for a number until the sum of the list of
#numbers is greater than 100.

list=[]
while(sum(list)<100):
    print('Enter a number still not reached 100')
    n=float(input())
    list.append(n)
