import random

comp = random.choice([-1,0,1])

print('''\n\t\t\t\tYOU'VE ENTERED THE GAME "SNAKE, WATER, GUN"!\n''')
print("Use the Following abbreviations: \n s: Snake\n w: Water \n g: Gun")

yourInput = input("\nChoose Snake, Water or Gun as per the abbreviations used: ")    

''' Here, we are assuming
'0' for water
'1' for Snake
'-1' for Gun
'''
assignments = {"s": 1, "w": 0, "g": -1}
you = assignments[yourInput]
reverseAllotment = {1:"Snake", 0:"Water", -1:"Gun"}

# printing the choices by you and comp
print(f"You chose '{reverseAllotment[you]}' \nComputer chose '{reverseAllotment[comp]}'")
print()
print("RESULT---> ", end="")

# Checking the win/lose case scenarios
if(you == comp):
    print("Hehe, It's a TIE between you and comp!")
else:
    if(comp == 1 and you == -1):
        print("CONGOO, You WON the match!")
    elif(comp == 1 and you == 0):
        print("SORRY, You LOST the match!")
    elif(comp == 0 and you == -1):
        print("SORRY, You LOST the match!")
    elif(comp == 0 and you == 1):
        print("CONGOO, You WON the match!")
    elif(comp == -1 and you == 1):
        print("SORRY, You LOST the match!")
    elif(comp == -1 and you == 0):
        print("CONGOO, You WON the match!")
    else:
        print("Something went wrong which is yet not programmed!")