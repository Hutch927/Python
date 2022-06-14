user_age: str = input("How old are you?")
user_age = int(user_age)
if user_age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote, better luck next year.")
