# Create a program that will play the "Cows and bulls" game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a "cow". For every digit the user guessed correctly in the wrong place
# is a "bull." Every time the user makes a guess, tell them how many "cows" and "bulls" they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game
# and tell the user at the end.

import random

# Initializing 4 digit non-repeating number
num = ""

while len(num) < 4:
    x = str(random.randint(0, 9))
    if x not in num:
        num = num + x

print(num)


# Method for user to input a number of 4 digits
def guesser():
    user = input("Choose a four digit number: ")
    if len(user) != 4:
        print("Please use only 4 digits")
        return guesser()
    return user


# Main method for the game
def game():
    count = 1
    user = guesser()
    while user != num:
        cow, bull = 0, 0
        for i in range(4):
            if user[i] == num[i]:
                cow += 1
            else:
                bull += 1
        print("Cows: " + str(cow) + " Bulls: " + str(bull))
        count += 1
        user = guesser()
    print("You got in " + str(count) + " tries.")


game()