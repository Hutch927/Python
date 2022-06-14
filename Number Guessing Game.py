import json
import random

def get_stored_username():
    """Tries to retrieve a stored username"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        pass
    else:
        return username

def get_new_username():
    """Prompts user for new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greets user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}!")
        un_check = input(f"\nIf you would like to continue enter 'y', if you are not {username.title()}, enter 'n': ")
        if un_check == "y":
            pass
        else:
            get_new_username()
    else:
        username = get_new_username()
        print(f"We will remember you next time {username}")

def get_stored_highscore():
    """Tries to get the users High Score."""
    filename = 'highscore.json'
    try:
        with open(filename, "r") as f:
            highScore = json.load(f)
            return highScore
    except FileNotFoundError:
        with open(filename, 'w') as f:
            json.dump(100, f)
            return 100
    else:
        return CurrentHighScore

def compare_highscore():
    """Compares high scores and stores the highest score."""
    highScore = get_stored_highscore()
    if int(CurrentHighScore) < int(highScore):
        print(f"Congratulations! You have a new high score of {CurrentHighScore}!")
        highscore = 'highscore.json'
        with open(highscore, "w") as f:
            json.dump(CurrentHighScore, f)
    else:
        print("Keep trying to get the high score!")
        print(f"The current highscore is {highScore}.")



number = random.randint(0, 25)
guess = 0
attempts = 0
user_guess = 00
#print (number)  # Line was used for testing only.

print(greet_user())

prompt = ("\nI am thinking of a number from 0 to 25, can you guess what it is?")
prompt += ("\nEnter 'quit' at any time to leave.")
print(prompt)

while True:
    user_guess = input('Please enter your guess: ')
    guess += 1
    attempts += 1
    if str(user_guess) == 'quit' or str(user_guess) == 'Quit':
        print('\nYou were unable to guess the number.')
        break
    elif len(str(user_guess)) < 1 or len(str(user_guess)) > 2:
        print("\nYour guess didn't have the right amount of numbers! 2 digits only.")
    elif int(user_guess) < number:
        print("\nYou need to guess higher!")
    elif int(user_guess) > number:
        print("\nYou need to guess lower!")
    elif int(user_guess) == number:
        print("\nYou Win!")
        break

print(f'The number was: {number}')
print(f'You made {attempts} attempts to get the correct number.')
CurrentHighScore = attempts
compare_highscore()




