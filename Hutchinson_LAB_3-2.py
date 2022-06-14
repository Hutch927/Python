# Make a list of 5 or more usernames, including the name 'admin'. Imagine you are writing code that will print a
# greeting to each user after they log into a website. loop through the list and print a greeting to each user.

usernames = ['newcoder25', 'hackerman1337', 'pythongeek1991', 'therealvanrossum', 'admin']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user}, would you like a status report?")
    else:
        print(f"Hello, {user}, thank you for logging in today!")

usernames = []

if usernames:
    for user in usernames:
        print(f'Hello, {user}, thank you for logging in today!')
else:
        print('We need to find more users!')
