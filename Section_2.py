#Brian Molina
#11/14/2022

#Section 2 of the game

def start():
    print("after watching the news and calling your friend...")
    print("You decide to head out and escape the building because there is a zombie horde")
    print("You pack things up and get backpack full on ready with snacks and food")
    print()
    print("What are your options?")
    print()
    choice = int(input("1. Get out silently  2. Wait for your friend so you both can go together  3. Get some food to eat while waiting for your friend "))
    print()
    if choice == 3:
        print("You get some food. You find some leftover pizza")
        print("===================================================")
        choice = input("Do you want pizza? Y/N")
        print("Yummy! Yummy! pizza!")
        print("===================================================")
        # If the player chooses pizza, he will eat it, if not, he will eat potato
    elif choice == 2:
        print("You wait for your friend!")
        print()
        # waiting because a zombie was on the left side outside waiting for Brian
        # to get out and eat him but happily he stayed.
    else:
        print("You get out. Didn't see there was a zombie to the left and killed you")
        print("=====================================================")
        print("You lose!")
        print()
        print("Game will now close")
        exit() # This stops the whole program
        #The player must wait for his friend so they both can go together
        #Or get some food to eat while waiting for the friend.
    import Section_3
    Section_3.start()
start()

