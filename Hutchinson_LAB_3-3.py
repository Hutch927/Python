# Create a program that simulates how websites ensure that everyone has a unique username.

current_users = ['newcoder25', 'hackerman1337', 'pythongeek1991', 'therealvanrossum', 'admin']
new_users = ['hackerman1337', 'therealvanrossum', 'freebird', 'pettytom15', 'bigtom45']

for user in new_users:
    if user in current_users or user.upper() in current_users or user.title() in current_users:
        print(f"The username, {user}, is currently in use. Please choose another.")
    else:
        print(f"The username,{user}, is available!")