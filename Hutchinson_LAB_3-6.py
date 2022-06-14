favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'} # starting dictionary
poll_takers = ['jen', 'phil', 'jackie', 'emily'] # created a list of possible poll takers

for name in poll_takers: # this for loop will run through the list of new names
    if name in favorite_languages.keys(): # if a name matches any of the keys, it will run the next line.
        print(f"You have already taken the survey {name.title()}! Thank you for your response.")
    else: # if a name does not match a key it will ask the user to take the survey.
        print(f"Please take our survey, {name.title()}, and tell us your favorite language!")

