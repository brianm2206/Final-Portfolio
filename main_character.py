#Brian Molina
#11/16/2022

#Code for the main character
class main_character:
    name = "Brian"
    friends_list = 1
    hp = 5
    money = 0
    weapon = 0

    def attack(self):
        print("You attack the zombie!")
        print("The zombie attacks you two and die")
        self.hp -= 5
