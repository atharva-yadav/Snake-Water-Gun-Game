# Snake, Water, Gun game using Python random module by atharva-yadav

import random
from playsound import playsound

def gameWin(comp, user):    # Function to decide win of user 

    # All possibilities if computer chooses Snake
    if comp == 's':
        if user == 's':
            return None
        elif user == 'w':
            return False
        elif user == 'g':
            return True

    # All possibilities if computer chooses Water
    if comp == 'w':
        if user == 's':
            return True
        elif user == 'w':
            return None
        elif user == 'g':
            return False

    # All possibilities if computer chooses Gun
    if comp == 'g':
        if user == 's':
            return False
        elif user == 'w':
            return True
        elif user == 'g':
            return None
    
print("Computer's turn")
r = random.randint(1,3)
if r == 1:
    comp = 's'
elif r == 2:
    comp = 'w'
elif r == 3:
    comp = 'g'

print("Your turn ")
user = input("Choose one out of Snake(s), Water(w), Gun(g)\n")

# Condition to avoid invalid entries
if(user != 's' and  user != 'S' and user != 'w' and user != 'W' and user != 'g' and user != 'G'):
    print("Invalid Input, Please select among s, w or g")
    exit()

print(f"Computer's option → {comp}")
print(f"Your's option → {user}")

result = gameWin(comp, user) # Function call

if(result == None):
    print("Match is tie")
    # Match tie sound generation using playsound module
    playsound('game-tie.mp3')

elif(result == False):
    print("You Lose :(")
    # Match tie sound generation using playsound module
    playsound('game-lose.mp3')

else:
    print("You Win :)")
    # Match tie sound generation using playsound module
    playsound('game-win.mp3')


