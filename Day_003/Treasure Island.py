print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

left_or_right = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\": ")

if left_or_right == "left":
    swim_or_wait = input("You've come to a lake. "
                         "There is an island in the middle of the lake. "
                         "Type \"wait\" to wait for a boat. "
                         "Type \"swim\" to swim across. ")
    if swim_or_wait.lower() == "wait":
        which_door = input("You arrive at the island unharmed. "
                           "There is a house with 3 doors. "
                           "One red, one yellow and one blue. "
                           "Which colour do you choose? ")
        if which_door.lower() == "yellow":
            print("You found the treasure! You Win!")
        elif which_door.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif which_door.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Game Over")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
