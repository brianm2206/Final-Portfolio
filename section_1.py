#Brian Molina
#11/14/2022

#Section 1 of the game
def start():
    print("You wake up all of a sudden in the living room, you don’t know what has happened to the world.")
    print("Bad people that got infected by someone")
    print("There is not much time!")
    print()
    print("What are you going to do?")
    choice = int(input("1. Get something to eat  2. Turn on the TV  5. Call friend"))

    if choice == 2:
        print("You watched the news. Found out something scary has happened.")
        #Because the user watched the TV.
        print("===================================================")
    elif choice == 1:
        print("You got something to eat but time is running out.")
        #the user shouldn't have done that
        print("===================================================")
    else:
        print("You called a friend asking about the news and what's happening")
        print("===================================================")
    import Section_2
    Section_2.start()
start()