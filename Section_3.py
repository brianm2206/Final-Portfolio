#Brian Molina
#11/14/2022

#Section 3 of the game
def start():
    print("After waiting for your friend, you open up the door very quietly so there is no noise and let your friend in")
    print("He goes inside with minor cut on his hand but no zombie bites...")
    print("which means he is not going to turn into a zombie")
    print("The friend starts telling the whole story and wants something to eat meanwhile help arrives.")
    print("A call can be made from the house phone.")
    print("What are your options?")
    choice = int(input("1. ask for the whole story of what happened  2. Watch a movie  3. Ask if he is hungry and give food."))
    print()
    if choice == 1:
        print("You want to ask for the story of what really happened")
        print("===================================================")
        choice = input("Do you want the complete story? Y/N")
        # If the player chooses complete story, he is going be be given the whole story
        # If not, he is going to receive the short story which would save time.
    elif choice == 2:
        print("You watched a movie but your friend got mad")
        print("===================================================")
        print("You lose because your friend does not play around!")
        print("Game will now close")
        exit()
        # He should have not watched a movie because it's a waste of time
    else:
        print("Give food to your friend")
        print("===================================================")
        print("He got full now!")
        # You gave leftover pizza to your friend.
    import section_4
    section_4.start()
start()