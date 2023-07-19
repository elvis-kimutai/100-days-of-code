print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'r at a crossroad where do you want to go? Type "left" or "Right" ').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake, there is an island in the middle. Type "wait " to wait for a boat, Type "Swim" to swim across ')
    if choice2 == "wait":
        choice3 = input('You have arrived to the island unharmed, There are three doors "red", "Yellow" and "Blue".Which do you choose ')
        if choice3 == "red":
            print("You got shot BASTED!! GAME OVER!!")
        elif choice3 == "Yellow":
            print("YESSS!!! You found the treasure!!. You win!")
        elif choice3 == "Blue":
            print("You got attacked by an angry beast GAME OVER!!")
        else:
            print("Door does not exist")
    else:
        print("Attacked by a crocodile. GAME OVER!!")
else:
    print("Fall into a hole. GAME OVER!!")