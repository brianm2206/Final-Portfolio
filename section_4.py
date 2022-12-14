#Brian Molina
#11/14/2022

#Section 4 of the game
def start():
    print("After finding out the whole story, you get scared.")
    print("you want to call emergency for help at getting out of the building and getting into a safe place.")
    print("The player uses the phone to call emergency.")
    print("What are your options?")
    choice = int(input("1. Call emergency for help  2. Call the pizza guy to order pizza  3. Call mom."))
    print()
    if choice == 1:
        print("You called emergency for help")
        print("===================================================")
        choice = input("Do you want help? Y/N")
        print("===================================================")
        print("Yay! You made it out alive!")
        print("I knew you two could do it!")
        exit()
        # If player says yes, he is going to get help
        # If not, he is going to die in that place along with his friend.
    elif choice == 2:
        print("You called but can't guarantee you will be receiving it.")
        print()
        print("If after 10 minutes had passed, that means he didn't make it")
        # calling the pizza guy and he is going to try to get it to you.
    else:
        print("You called mom but does not answer.")
        # Could be that she left to another place already.