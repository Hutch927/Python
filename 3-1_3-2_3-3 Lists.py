#Working with lists
names = ['amy', 'maggie', 'freddie', 'tyler', 'rachel', 'jon', 'ruth'] #Created a list and stored names of friends
motorcycles = ['triumph', 'honda', 'harley', 'indian'] #stored names of motorcycles

print(names) #print all the names and not formated
print(motorcycles) #prints motorcycle list


print(names[0].title()) #Calls the first name and prints with title case. 

print(f"{names[0].title()}, I hope you have a wonderful day!") #fstring used to print a personalized message.
print(f"{names[1].title()}, you are 3 years old!") #fstring used to print a personalized message.

print(f"I currently ride a {motorcycles[0].title()}, but would like to own an {motorcycles[-1].title()} Chieftan.")

motorcycles[0] = 'suzuki' #this changes the 1st item in the list to something new
print(motorcycles)#print to test

motorcycles.append('yamaha') #appended the list and added an item to the end.
print(motorcycles) #print to test

motorcycles.insert( 0, 'triumph' ) #added an item to the begining of the list.
print(motorcycles)


